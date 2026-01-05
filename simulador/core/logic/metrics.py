from typing import List, Dict

from .process import Process


def calculate_metrics(processes: List[Process]) -> Dict[str, float]:
	"""Calcula promedios de Waiting Time, Turnaround Time y Response Time.

	Devuelve un dict con claves: avg_wt, avg_tat, avg_rt y totals.
	"""
	n = len(processes)
	if n == 0:
		return {
			"avg_wt": 0.0,
			"avg_tat": 0.0,
			"avg_rt": 0.0,
			"total_wt": 0.0,
			"total_tat": 0.0,
			"total_rt": 0.0,
		}
	
	total_wt = 0.0
	total_tat = 0.0
	total_rt = 0.0

	for p in processes:
		if p.turn_around_time is None:
			# intentar calcular si completion_time está definida
			if p.completion_time is not None:
				p.turn_around_time = p.completion_time - p.arrival_time
			else:
				raise ValueError(f"Proceso {p.pid} no completado, no se pueden calcular métricas")

		if p.response_time is None:
			# Si el proceso nunca fue ejecutado, response_time debería ser 0
			# ya que todos los procesos en una simulación completa deben ejecutarse
			p.response_time = 0

		total_wt += p.waiting_time
		total_tat += p.turn_around_time
		total_rt += p.response_time

	return {
		"avg_wt": total_wt / n,
		"avg_tat": total_tat / n,
		"avg_rt": total_rt / n,
		"total_wt": total_wt,
		"total_tat": total_tat,
		"total_rt": total_rt,
	}


__all__ = ["calculate_metrics"]

