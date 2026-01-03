from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from core.logic.process import Process
from core.logic.fcfs import fcfs_schedule
from core.logic.sjf import sjf_schedule
from core.logic.round_robin import round_robin_schedule
from core.logic.priority import priority_schedule
from core.logic.metrics import calculate_metrics


@require_http_methods(["GET"])
def index(request):
	"""Render the form to create/select processes and choose algorithm.

	GET clears session so page reload resets the form.
	"""
	# clear stored session values so reloading the main page resets the form
	request.session.pop('processes', None)
	request.session.pop('algorithm', None)
	request.session.pop('quantum', None)
	return render(request, 'index.html', {'submitted': None})


@require_http_methods(["POST"])
def run_simulator(request):
	"""Parse submitted form, run selected scheduler and render results."""
	pids = request.POST.getlist('pid')
	arrivals = request.POST.getlist('arrival_time')
	bursts = request.POST.getlist('burst_time')
	priorities = request.POST.getlist('priority')

	processes = []
	for i in range(len(pids)):
		try:
			processes.append(Process(pid=int(pids[i]), arrival_time=int(arrivals[i]), burst_time=int(bursts[i]), priority=int(priorities[i]) if i < len(priorities) and priorities[i] != '' else 0))
		except (ValueError, IndexError):
			continue

	algorithm = request.POST.get('algorithm')
	quantum = request.POST.get('quantum')
	# run chosen algorithm
	if algorithm == 'fcfs':
		result = fcfs_schedule(processes)
	elif algorithm == 'sjf':
		result = sjf_schedule(processes)
	elif algorithm == 'rr':
		q = int(quantum) if quantum else 1
		result = round_robin_schedule(processes, quantum=q)
	elif algorithm == 'priority':
		result = priority_schedule(processes)
	else:
		# unknown algorithm: redirect back
		return redirect('index')

	metrics = calculate_metrics(result)
	# convert processes to dicts for template
	procs_data = [p.to_dict() for p in result]
	# additional timeline metrics for Gantt
	# find timeline bounds
	min_t = None
	max_t = None
	for p in procs_data:
		for seg in p.get('history', []):
			if min_t is None or seg['start'] < min_t:
				min_t = seg['start']
			if max_t is None or seg['end'] > max_t:
				max_t = seg['end']
	if min_t is None:
		min_t = 0
	if max_t is None:
		max_t = 0

	# makespan, total busy, idle, utilization, throughput
	makespan = max_t - min_t
	total_busy = sum((p['burst_time'] for p in procs_data))
	total_idle = max(0, makespan - total_busy) if makespan > 0 else 0
	cpu_util = (total_busy / makespan) * 100 if makespan > 0 else 0
	throughput = (len(procs_data) / makespan) if makespan > 0 else 0

	context = {
		'algorithm': algorithm,
		'quantum': quantum,
		'metrics': metrics,
		'processes': procs_data,
		'timeline_min': min_t,
		'timeline_max': max_t,
		'makespan': makespan,
		'total_busy': total_busy,
		'total_idle': total_idle,
		'cpu_util': round(cpu_util, 2),
		'throughput': round(throughput, 3),
	}
	return render(request, 'results.html', context)
