from core.base.Algorithm import Algorithm
from core.base.Process import Process, ProcessState
from core.implementations.PO.ProcessUpdate import ProcessUpdate
from core.implementations.PO.Log import Log
from core.implementations.PO.Timestamp import Timestamp, TimestampState
from time import sleep

class RoundRobin(Algorithm):
    
    def execute(self, *args, **kwargs):
        self.quantum = kwargs.get('quantum', 5)
        self.process_stack = kwargs.get('process_stack', [])

        leftover_time = 0
        yield Timestamp(TimestampState.START)
        while len(self.process_stack) > 0:
            # Do work on one at a time x quantum
            updates = []
            for i, process in enumerate(self.process_stack):
                sleep(0.5)  # Simulate time passing
                state, leftover_time = process.update(leftover_time, self.quantum)
                updates.append((state, leftover_time))

                if state == ProcessState.TERMINATED:
                    self.process_stack.pop(i)
                    yield ProcessUpdate(process.pid, process.remaining_time, ProcessState.TERMINATED)

                elif state == ProcessState.STARVED:
                    self.process_stack.pop(i)
                    yield ProcessUpdate(process.pid, process.remaining_time, ProcessState.STARVED)
                
                else:
                    yield ProcessUpdate(process.pid, process.remaining_time, ProcessState.ALIVE)

        yield Timestamp(TimestampState.END)
