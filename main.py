from core.base.Executor import Executable
from core.implementations.PO.PollLog import PollLog
from threading import Thread


class AlgorithServiceSingleton:
    _instance = None

    def __new__(cls, algorithm: Executable):
        if cls._instance is None:
            cls._instance = super(AlgorithServiceSingleton, cls).__new__(cls)
            cls._instance.algorithm = algorithm
        return cls._instance

    def __init__(self, algorithm: Executable):
        self.running = False
        self.algorithm = algorithm
        self.logs = []

    def pollLogs(self) -> list[str]:
        return self.logs
    
    def run(self, *args, **kwargs) -> None:
        thread = Thread(target=self.execute, args=args, kwargs=kwargs)
        thread.start()
        return thread

    def execute(self, *args, **kwargs):
        self.logs = []
        if not self.running:
            self.running = True
            for yielded in self.algorithm.execute(*args, **kwargs):
                if isinstance(yielded, PollLog):
                    self.logs.append(yielded.message)
            self.running = False

    @classmethod
    def getInstance(cls, algorithm: Executable = None):
        if algorithm is None and cls._instance is None:
            return None
        
        elif cls._instance is None:
            cls._instance = AlgorithServiceSingleton(algorithm)
        return cls._instance
    
    def is_running(self) -> bool:
        return self.running