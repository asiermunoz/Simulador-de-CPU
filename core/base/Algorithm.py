from .Executor import Executable

class Algorithm(Executable):
    def __init__(self):
        super().__init__()
    
    """ Execute is the default run procedure for the algorithm. """
    def execute(self, *args, **kwargs):
        print(f"Executing {self.getSignature()}")