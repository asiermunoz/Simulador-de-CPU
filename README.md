# Simulador-de-CPU

Simulador de algoritmos de planificación de CPU desarrollado en Python 3.14 con Django como framework para la interfaz web. Este proyecto es parte del curso de Sistemas Operativos.

## Características

- **Algoritmos Implementados:**
  - FCFS (First-Come, First-Served)
  - SJF (Shortest Job First)
  - Round Robin
  - Planificación por Prioridad

- **Funcionalidades:**
  - Entrada manual de procesos
  - Carga de procesos desde archivo CSV
  - Modo de comparación entre algoritmos
  - Visualización de diagrama de Gantt
  - Cálculo de métricas (tiempo de espera, tiempo de retorno, tiempo de respuesta)
  - Cálculo de utilización de CPU

## Formato de Archivo CSV

El archivo debe contener una línea por proceso con el siguiente formato:
```
PID,Tiempo_Llegada,Tiempo_Ráfaga,Prioridad
```

Ejemplo (`ejemplo_procesos.csv`):
```csv
# Este es un comentario (las líneas que empiezan con # se ignoran)
1,0,8,2
2,1,4,1
3,2,9,3
4,3,5,2
```

**Notas:**
- El campo Prioridad es opcional (por defecto es 0)
- Menor valor de prioridad = mayor prioridad
- Las líneas vacías y comentarios se ignoran
- Tamaño máximo de archivo: 1MB

## Instalación y Uso

1. Clonar el repositorio:
```bash
git clone https://github.com/asiermunoz/Simulador-de-CPU.git
cd Simulador-de-CPU
```

2. Instalar dependencias:
```bash
pip install django
```

3. Ejecutar el servidor:
```bash
cd simulador
python manage.py runserver
```

4. Abrir en el navegador:
```
http://localhost:8000
```

## Ejecución de Tests

```bash
# Test básico de algoritmos
python tests/run_algorithms.py

# Tests de casos límite
python tests/test_edge_cases.py
```

## Validaciones Implementadas

- ✓ Validación de tamaño de archivo (máximo 1MB)
- ✓ Validación de formato UTF-8
- ✓ Validación de datos numéricos
- ✓ Validación de quantum > 0 para Round Robin
- ✓ Validación de burst_time > 0
- ✓ Validación de arrival_time >= 0
- ✓ Manejo robusto de errores con mensajes informativos

## Estructura del Proyecto

```
Simulador-de-CPU/
├── simulador/
│   ├── core/
│   │   ├── logic/           # Algoritmos de planificación
│   │   │   ├── process.py   # Clase Process
│   │   │   ├── fcfs.py      # FCFS
│   │   │   ├── sjf.py       # SJF
│   │   │   ├── round_robin.py  # Round Robin
│   │   │   ├── priority.py  # Prioridad
│   │   │   └── metrics.py   # Cálculo de métricas
│   │   ├── views.py         # Controladores Django
│   │   └── templates/       # Plantillas HTML
│   └── manage.py
└── tests/                   # Tests automatizados
```

## Contribuciones

Las mejoras implementadas en este proyecto incluyen:
- Manejo robusto de errores
- Validación exhaustiva de entradas
- Documentación completa con docstrings
- Tests de casos límite
- Seguridad mejorada en carga de archivos

