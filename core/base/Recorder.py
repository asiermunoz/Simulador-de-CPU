from .Executor import Executable

class Recorder(Executable):
    def __init__(self, decoratee = None):
        super().__init__()
        self.decoratee = decoratee
    
    def execute(self, *args, **kwargs):
        print(f"[RECORDER]: Recorded execution with args: {args} and kwargs: {kwargs}")
        if self.decoratee:
            for message in self.decoratee.execute(*args, **kwargs):
                self.processData(message)
                yield message    

    def processData(self, data):
        print(f"[RECORDER]: Processing data: {data}")