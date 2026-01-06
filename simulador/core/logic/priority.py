from typing import List
import copy

from .process import Process
def priority_schedule(processes: List[Process]) -> List[Process]:
	"""Simulación de planificación por prioridad (no preemptiva).

	Selecciona siempre el proceso listo con mayor prioridad.
	IMPORTANTE: menor valor numérico de priority = mayor prioridad.
	Por ejemplo: priority=1 tiene mayor prioridad que priority=3.

	Args:
		processes: Lista de procesos a planificar.

	Returns:
		Lista de procesos completados (orden de finalización).
	"""
	if not processes:
		return []
	
	procs = [copy.deepcopy(p) for p in processes]
	procs.sort(key=lambda p: p.sort_key_arrival())

	n = len(procs)
	ready: List[Process] = []
	completed: List[Process] = []
	idx = 0
	current_time = 0

	while len(completed) < n:
		while idx < n and procs[idx].arrival_time <= current_time:
			ready.append(procs[idx])
			idx += 1

		if not ready:
			if idx < n:
				current_time = procs[idx].arrival_time
				continue
			else:
				break

		# ordenar por prioridad (menor primero), luego llegada, luego pid
		ready.sort(key=lambda p: (p.priority, p.arrival_time, p.pid))
		p = ready.pop(0)
		p.execute(p.remaining_time, current_time)
		current_time = p.completion_time or current_time
		completed.append(p)

	return completed


__all__ = ["priority_schedule"]
