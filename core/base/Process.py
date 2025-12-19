from random import randint

class Process:
    def __init__(self, pid: int, starve_time: int, remaining_time: int = 0):
        self.pid = pid
        self.starve_time = starve_time
        self.remaining_time = remaining_time

    def will_starve(self, update: int) -> bool:
        return self.starve_time - update <= 0
    
    def will_complete(self, update: int) -> bool:
        return self.remaining_time - update <= 0
    
    def update(self, elapsed_time: int, delta_time: int) -> tuple[int, int]:
        """ 
        Update the starve time of the process. 
        Returns the new state of the process and the remaining time left (if any).
        """
        if (self.will_starve(elapsed_time)):
            self.starve_time = 0
            return (ProcessState.STARVED, abs(self.starve_time))
        else:
            self.starve_time -= elapsed_time
        
        if (self.will_complete(delta_time)):
            self.remaining_time = 0
            return (ProcessState.TERMINATED, abs(self.remaining_time))
        else:
            self.remaining_time -= delta_time

        return (ProcessState.ALIVE, 0)
    
    @staticmethod
    def fromList(data: list[int]) -> list["Process"]:
        result = []
        for i, remaining_time in enumerate(data):
            result.append(Process(pid=i, starve_time=randint(5,15), remaining_time=remaining_time))
        
        return result


class ProcessState:
    ALIVE = 0
    DEAD = 1
    STARVED = 2
    TERMINATED = 3

    @classmethod
    def toString(cls, state: int) -> str:
        if state == cls.ALIVE:
            return "ALIVE"
        elif state == cls.DEAD:
            return "DEAD"
        elif state == cls.STARVED:
            return "STARVED"
        elif state == cls.TERMINATED:
            return "TERMINATED"
        else:
            return ValueError("UNKNOWN PROCESS STATE")