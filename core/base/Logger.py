from .Executor import Executable
from ..implementations.PO.Log import Log

class Logger(Executable): 
    def execute(self, *args, **kwargs):
        if self.decoratee:
            for message in self.decoratee.execute(*args, **kwargs):
                if isinstance(message, Log):
                    yield self.log(message.message)
                else:
                    yield message
                     
    def log(self, message: str):
        pass
