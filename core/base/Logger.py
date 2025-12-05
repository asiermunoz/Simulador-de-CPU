from .Executor import Executable

class Logger(Executable):
    def __init__(self, decoratee = None):
        super().__init__()
        self.decoratee = decoratee
    
    def execute(self, *args, **kwargs):
        if self.decoratee:
            print(f"[LOG]: Calling {self.decoratee.getSignature()}")
            for message in self.decoratee.execute(*args, **kwargs):
                if not isinstance(message, str):
                    yield message
                else:
                    print(f"[LOG]: yielded {message}")
        else:
            print(f"[LOG]: {self.getSignature()} not configured correctly")
