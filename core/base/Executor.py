class Executable:
    def __init__(self, decoratee = None):
        self.decoratee = decoratee

    
    def execute(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        return list(self.execute(*args, **kwargs) or [])
    
    def getSignature(self):
        return self.__class__.__name__