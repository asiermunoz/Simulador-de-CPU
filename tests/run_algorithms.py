import os
import sys

# ensure project root is on sys.path so imports work when running this script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulador.core.logic.process import Process
from simulador.core.logic.fcfs import fcfs_schedule
from simulador.core.logic.sjf import sjf_schedule
from simulador.core.logic.round_robin import round_robin_schedule
from simulador.core.logic.priority import priority_schedule
from simulador.core.logic.metrics import calculate_metrics


def make_processes():
    return [
        Process(pid=1, arrival_time=0, burst_time=8, priority=2),
        Process(pid=2, arrival_time=1, burst_time=4, priority=1),
        Process(pid=3, arrival_time=2, burst_time=9, priority=3),
        Process(pid=4, arrival_time=3, burst_time=5, priority=2),
    ]


def run():
    procs = make_processes()

    print("== FCFS ==")
    res = fcfs_schedule(procs)
    print(calculate_metrics(res))
    for p in res:
        print(p.to_dict())

    print("\n== SJF ==")
    res = sjf_schedule(procs)
    print(calculate_metrics(res))
    for p in res:
        print(p.to_dict())

    print("\n== Round Robin (quantum=3) ==")
    res = round_robin_schedule(procs, quantum=3)
    print(calculate_metrics(res))
    for p in res:
        print(p.to_dict())

    print("\n== Priority ==")
    res = priority_schedule(procs)
    print(calculate_metrics(res))
    for p in res:
        print(p.to_dict())


if __name__ == '__main__':
    run()
