from typing import List
import copy

from .process import Process
def sjf_schedule(processes: List[Process]) -> List[Process]:
	"""Simulación SJF no preemptiva.

	Selecciona el proceso con menor `burst_time` entre los listos.
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
		# añadir procesos que hayan llegado
		while idx < n and procs[idx].arrival_time <= current_time:
			ready.append(procs[idx])
			idx += 1

		if not ready:
			# saltar al siguiente proceso que llegue
			if idx < n:
				current_time = procs[idx].arrival_time
				continue
			else:
				break

		# elegir el de menor burst_time
		ready.sort(key=lambda p: (p.burst_time, p.arrival_time, p.pid))
		p = ready.pop(0)
		p.execute(p.remaining_time, current_time)
		current_time = p.completion_time or current_time
		completed.append(p)

	return completed


__all__ = ["sjf_schedule"]
