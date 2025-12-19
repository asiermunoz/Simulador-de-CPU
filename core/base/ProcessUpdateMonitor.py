from core.base.Executor import Executable
from core.implementations.PO.ProcessUpdate import ProcessUpdate
from core.base.Process import ProcessState

from core.implementations.PO.Log import Log

class ProcessUpdateMonitor(Executable):
    def execute(self, *args, **kwargs):
        if self.decoratee:
            for message in self.decoratee.execute(*args, **kwargs):
                if isinstance(message, ProcessUpdate):
                    yield self.notify(message)    
                else:
                    yield message

    def notify(self, data: ProcessUpdate):
        return Log(f"Process Update - PID: {data.pid}, Remaining Time: {data.remaining_time}, State: {ProcessState.toString(data.state)}")