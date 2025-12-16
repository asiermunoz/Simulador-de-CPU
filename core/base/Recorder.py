from core.implementations.PO.Timestamp import Timestamp
from .Executor import Executable

class Recorder(Executable):
    def execute(self, *args, **kwargs):
        if self.decoratee:
            for message in self.decoratee.execute(*args, **kwargs):
                if not isinstance(message, Timestamp):
                     yield message
                else:
                    self.processData(message)    

    def processData(self, data):
        print(f"[RECORDER]: Processing data: {data}")