from typing import List
import copy

from .process import Process


def fcfs_schedule(processes: List[Process]) -> List[Process]:
	"""Simulación FCFS (First-Come, First-Served) no preemptiva.

	Ejecuta los procesos en orden de llegada sin interrupción.
	Los procesos se ordenan por tiempo de llegada y se ejecutan
	secuencialmente hasta completarse.

	Args:
		processes: Lista de procesos a planificar.

	Returns:
		Lista de procesos con campos de tiempo completados (en orden de llegada).
	"""
	if not processes:
		return []
	
	procs = [copy.deepcopy(p) for p in processes]
	procs.sort(key=lambda p: p.sort_key_arrival())

	current_time = 0
	for p in procs:
		if current_time < p.arrival_time:
			current_time = p.arrival_time
		p.execute(p.remaining_time, current_time)
		# p.completion_time set by execute()
		current_time = p.completion_time or current_time

	return procs


__all__ = ["fcfs_schedule"]
