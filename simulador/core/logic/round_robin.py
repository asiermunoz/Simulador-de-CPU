from typing import List

# Round Robin implementation goes here
from typing import List
from collections import deque
import copy

from .process import Process


def round_robin_schedule(processes: List[Process], quantum: int) -> List[Process]:
	"""Simulación Round-Robin preemptiva con quantum dado.

	Devuelve la lista de procesos completados (orden de finalización).
	"""
	if quantum <= 0:
		raise ValueError("quantum debe ser > 0")

	procs = [copy.deepcopy(p) for p in processes]
	procs.sort(key=lambda p: p.sort_key_arrival())

	n = len(procs)
	idx = 0
	current_time = 0
	queue = deque()
	completed: List[Process] = []

	while len(completed) < n:
		# encolar llegadas
		while idx < n and procs[idx].arrival_time <= current_time:
			queue.append(procs[idx])
			idx += 1

		if not queue:
			if idx < n:
				current_time = procs[idx].arrival_time
				continue
			else:
				break

		p = queue.popleft()
		executed = p.execute(quantum, current_time)
		current_time += executed

		# encolar nuevas llegadas ocurridas durante la ejecución
		while idx < n and procs[idx].arrival_time <= current_time:
			queue.append(procs[idx])
			idx += 1

		if p.is_finished():
			completed.append(p)
		else:
			queue.append(p)

	return completed


__all__ = ["round_robin_schedule"]
