from .Executor import Executable
from ..implementations.PO.Log import Log

class Logger(Executable): 
    def execute(self, *args, **kwargs):
        if self.decoratee:
            for message in self.decoratee.execute(*args, **kwargs):
                if not isinstance(message, Log):
                    yield message
                else:
                    print(f"\n[LOG]: {message}")
