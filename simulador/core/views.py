from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from core.logic.process import Process
# Importación de algoritmos y métricas
from core.logic.fcfs import fcfs_schedule
from core.logic.sjf import sjf_schedule
from core.logic.round_robin import round_robin_schedule
from core.logic.priority import priority_schedule
from core.logic.metrics import calculate_metrics

@require_http_methods(["GET"])
def index(request):
    """
    Renderiza la página principal con el formulario de configuración.
    Limpia cualquier estado previo de la sesión.
    """
    return render(request, 'index.html')

@require_http_methods(["POST"])
def run_simulator(request):
    """
    Controlador principal de la simulación.
    1. Procesa la entrada (Archivo o Manual).
    2. Selecciona el modo de ejecución (Individual o Comparativo).
    3. Ejecuta los algoritmos correspondientes.
    4. Renderiza la plantilla de resultados.
    """
    processes = []
    
    # ---------------------------------------------------------
    # 1. MÓDULO DE CARGA DE DATOS
    # ---------------------------------------------------------
    if 'process_file' in request.FILES:
        # Procesamiento de archivo cargado (CSV/TXT)
        uploaded_file = request.FILES['process_file']
        
        # Validar tamaño del archivo (máximo 1MB)
        if uploaded_file.size > 1024 * 1024:
            return render(request, 'index.html', {'error': "El archivo es demasiado grande. Máximo 1MB."})
        
        try:
            file_data = uploaded_file.read().decode('utf-8').splitlines()
            for line_num, line in enumerate(file_data, 1):
                line = line.strip()
                if not line or line.startswith('#'):  # Ignorar líneas vacías y comentarios
                    continue
                try:
                    parts = line.split(',')
                    if len(parts) >= 3:
                        # Formato esperado: PID, Arrival, Burst, [Priority]
                        pid = int(parts[0])
                        arr = int(parts[1])
                        burst = int(parts[2])
                        pri = int(parts[3]) if len(parts) > 3 else 0
                        processes.append(Process(pid=pid, arrival_time=arr, burst_time=burst, priority=pri))
                except (ValueError, IndexError) as e:
                    return render(request, 'index.html', {'error': f"Error en línea {line_num}: formato inválido."})
        except UnicodeDecodeError:
            return render(request, 'index.html', {'error': "Error: el archivo debe estar codificado en UTF-8."})
        except Exception:
            return render(request, 'index.html', {'error': "Error al procesar el archivo. Verifica el formato."})
    
    # Si no hay archivo, intentar carga manual del formulario
    if not processes:
        pids = request.POST.getlist('pid')
        arrivals = request.POST.getlist('arrival_time')
        bursts = request.POST.getlist('burst_time')
        priorities = request.POST.getlist('priority')
        
        for i in range(len(pids)):
            try:
                p = Process(
                    pid=int(pids[i]), 
                    arrival_time=int(arrivals[i]), 
                    burst_time=int(bursts[i]), 
                    priority=int(priorities[i]) if i < len(priorities) and priorities[i] != '' else 0
                )
                processes.append(p)
            except (ValueError, IndexError, TypeError):
                continue

    if not processes:
         return render(request, 'index.html', {'error': "No se proporcionaron procesos válidos."})

    algorithm = request.POST.get('algorithm')
    try:
        quantum_val = int(request.POST.get('quantum', 3))
        if quantum_val <= 0:
            quantum_val = 3
    except (ValueError, TypeError):
        quantum_val = 3

    # ---------------------------------------------------------
    # 2. MODO COMPARACIÓN (Requerimiento de Análisis)
    # ---------------------------------------------------------
    if algorithm == 'compare':
        results_list = []
        
        # Definición de escenarios a comparar
        scenarios = [
            ('FCFS', fcfs_schedule(processes)),
            ('SJF', sjf_schedule(processes)),
            ('Priority', priority_schedule(processes)),
            ('Round Robin (Q=' + str(quantum_val) + ')', round_robin_schedule(processes, quantum=quantum_val))
        ]

        best_wt = float('inf')
        winner_wt = ""
        best_tat = float('inf')
        winner_tat = ""

        # Ejecución y cálculo de métricas para cada algoritmo
        for name, procs_result in scenarios:
            metrics = calculate_metrics(procs_result)
            results_list.append({'name': name, 'metrics': metrics})
            
            # Determinar ganador basado en Tiempo de Espera (Waiting Time)
            if metrics['avg_wt'] < best_wt:
                best_wt = metrics['avg_wt']
                winner_wt = name
            if metrics['avg_tat'] < best_tat:
                best_tat = metrics['avg_tat']
                winner_tat = name

        return render(request, 'comparison.html', {
            'results': results_list,
            'winner_wt': winner_wt,
            'winner_tat': winner_tat
        })

    # ---------------------------------------------------------
    # 3. MODO INDIVIDUAL (Ejecución simple)
    # ---------------------------------------------------------
    try:
        if algorithm == 'fcfs':
            result = fcfs_schedule(processes)
        elif algorithm == 'sjf':
            result = sjf_schedule(processes)
        elif algorithm == 'rr':
            result = round_robin_schedule(processes, quantum=quantum_val)
        elif algorithm == 'priority':
            result = priority_schedule(processes)
        else:
            return render(request, 'index.html', {'error': "Algoritmo no válido."})

        # Cálculo final de métricas y preparación de datos para Gantt
        metrics = calculate_metrics(result)
        procs_data = [p.to_dict() for p in result]
    except Exception as e:
        return render(request, 'index.html', {'error': "Error al ejecutar la simulación."})
    
    # Determinar límites del timeline para visualización
    min_t = min((seg['start'] for p in procs_data for seg in p.get('history', [])), default=0)
    max_t = max((seg['end'] for p in procs_data for seg in p.get('history', [])), default=0)
    
    makespan = max_t - min_t
    total_busy = sum(p['burst_time'] for p in procs_data)
    cpu_util = (total_busy / makespan * 100) if makespan > 0 else 0

    context = {
        'algorithm': algorithm,
        'quantum': quantum_val,
        'metrics': metrics,
        'processes': procs_data,
        'timeline_min': min_t,
        'timeline_max': max_t,
        'makespan': makespan,
        'total_busy': total_busy,
        'total_idle': max_t - min_t - total_busy,
        'cpu_util': round(cpu_util, 2),
    }
    return render(request, 'results.html', context)