from core.base.ParameterObject import ParameterObject

class PollLog(ParameterObject):
    def __init__(self, message: str):
        super().__init__()
        self.message = message
    