"""
Tests para validar casos límite y mejoras de código.
"""
import os
import sys

# Asegurar que el directorio raíz del proyecto esté en sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulador.core.logic.process import Process
from simulador.core.logic.fcfs import fcfs_schedule
from simulador.core.logic.sjf import sjf_schedule
from simulador.core.logic.round_robin import round_robin_schedule
from simulador.core.logic.priority import priority_schedule
from simulador.core.logic.metrics import calculate_metrics


def test_empty_process_list():
    """Verifica que las funciones manejen listas vacías correctamente."""
    print("Test: Lista vacía de procesos")
    
    empty_list = []
    
    # Todos los algoritmos deben retornar lista vacía
    assert fcfs_schedule(empty_list) == []
    assert sjf_schedule(empty_list) == []
    assert priority_schedule(empty_list) == []
    assert round_robin_schedule(empty_list, quantum=3) == []
    
    # Las métricas deben retornar ceros
    metrics = calculate_metrics(empty_list)
    assert metrics['avg_wt'] == 0.0
    assert metrics['avg_tat'] == 0.0
    assert metrics['avg_rt'] == 0.0
    
    print("✓ Test de lista vacía pasó correctamente")


def test_invalid_quantum():
    """Verifica que quantum inválido lance excepción."""
    print("Test: Quantum inválido")
    
    processes = [Process(pid=1, arrival_time=0, burst_time=5)]
    
    try:
        round_robin_schedule(processes, quantum=0)
        assert False, "Debería lanzar ValueError"
    except ValueError as e:
        assert "quantum debe ser > 0" in str(e)
        print("✓ ValueError lanzado correctamente para quantum=0")
    
    try:
        round_robin_schedule(processes, quantum=-1)
        assert False, "Debería lanzar ValueError"
    except ValueError as e:
        assert "quantum debe ser > 0" in str(e)
        print("✓ ValueError lanzado correctamente para quantum=-1")


def test_invalid_process_data():
    """Verifica validación de datos de proceso."""
    print("Test: Datos de proceso inválidos")
    
    # burst_time debe ser positivo
    try:
        Process(pid=1, arrival_time=0, burst_time=0)
        assert False, "Debería lanzar ValueError para burst_time=0"
    except ValueError as e:
        assert "burst_time debe ser positivo" in str(e)
        print("✓ ValueError lanzado correctamente para burst_time=0")
    
    # arrival_time no debe ser negativo
    try:
        Process(pid=1, arrival_time=-1, burst_time=5)
        assert False, "Debería lanzar ValueError para arrival_time negativo"
    except ValueError as e:
        assert "arrival_time debe ser no negativo" in str(e)
        print("✓ ValueError lanzado correctamente para arrival_time negativo")


def test_single_process():
    """Verifica que un solo proceso se maneje correctamente."""
    print("Test: Un solo proceso")
    
    single = [Process(pid=1, arrival_time=0, burst_time=10)]
    
    # Todos los algoritmos deben dar el mismo resultado con un solo proceso
    result_fcfs = fcfs_schedule(single)
    result_sjf = sjf_schedule(single)
    result_priority = priority_schedule(single)
    result_rr = round_robin_schedule(single, quantum=3)
    
    # Verificar que el proceso se completó
    assert len(result_fcfs) == 1
    assert result_fcfs[0].completion_time == 10
    assert result_fcfs[0].waiting_time == 0
    assert result_fcfs[0].turn_around_time == 10
    
    print("✓ Test de un solo proceso pasó correctamente")


def test_processes_same_arrival():
    """Verifica comportamiento con procesos que llegan al mismo tiempo."""
    print("Test: Procesos con mismo tiempo de llegada")
    
    processes = [
        Process(pid=1, arrival_time=0, burst_time=8, priority=3),
        Process(pid=2, arrival_time=0, burst_time=4, priority=1),
        Process(pid=3, arrival_time=0, burst_time=6, priority=2),
    ]
    
    # SJF debe ejecutar primero el más corto (pid=2)
    result_sjf = sjf_schedule(processes)
    assert result_sjf[0].pid == 2
    assert result_sjf[0].burst_time == 4
    
    # Priority debe ejecutar primero el de menor valor (pid=2, priority=1)
    result_priority = priority_schedule(processes)
    assert result_priority[0].pid == 2
    assert result_priority[0].priority == 1
    
    print("✓ Test de procesos simultáneos pasó correctamente")


def run_all_tests():
    """Ejecuta todos los tests de casos límite."""
    print("=" * 60)
    print("EJECUTANDO TESTS DE CASOS LÍMITE")
    print("=" * 60)
    
    test_empty_process_list()
    test_invalid_quantum()
    test_invalid_process_data()
    test_single_process()
    test_processes_same_arrival()
    
    print("=" * 60)
    print("TODOS LOS TESTS PASARON EXITOSAMENTE ✓")
    print("=" * 60)


if __name__ == '__main__':
    run_all_tests()
