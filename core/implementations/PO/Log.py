from core.base.ParameterObject import ParameterObject

class Log(ParameterObject):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)