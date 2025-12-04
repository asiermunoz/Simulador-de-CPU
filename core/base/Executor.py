class Executable:
    def __init__(self):
        pass
    
    def execute(self, *args, **kwargs):
        pass

    def getSignature(self):
        return self.__class__.__name__