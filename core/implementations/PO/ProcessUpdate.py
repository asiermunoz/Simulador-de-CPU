from core.base.ParameterObject import ParameterObject

class ProcessUpdate(ParameterObject):
    def __init__(self, pid: int, remaining_time: int, state: int):
        self.pid = pid
        self.remaining_time = remaining_time
        self.state = state