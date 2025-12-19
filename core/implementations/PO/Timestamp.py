from core.base.ParameterObject import ParameterObject

class TimestampState:
    START = 0
    END = 1
    PAUSE = 2
    RESUME = 3

    @classmethod
    def toString(cls, state: int) -> str:
        if state == cls.START:
            return "START"
        elif state == cls.END:
            return "END"
        elif state == cls.PAUSE:
            return "PAUSE"
        elif state == cls.RESUME:
            return "RESUME"
        else:
            raise ValueError("Invalid TimestampState integer value")

class Timestamp(ParameterObject):
    def __init__(self, timestamp: TimestampState | int):
        self.timestamp = timestamp

    def __str__(self):
        return TimestampState.toString(self.timestamp) if isinstance(self.timestamp, int) else str(self.timestamp)
    
    