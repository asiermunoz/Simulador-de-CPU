from .Executor import Executable

class Logger(Executable):
    def __init__(self, decoratee = None):
        super().__init__()
        self.decoratee = decoratee
    
    def execute(self):
        print("running")
        if self.decoratee:
            print(f"[LOG]: Calling {self.decoratee.getSignature()}")
            self.decoratee.execute()
        else:
            print(f"[LOG]: {self.getSignature()} not configured correctly")


