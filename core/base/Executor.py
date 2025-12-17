class Executable:
    def __init__(self, decoratee = None):
        self.decoratee = decoratee

    
    def execute(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        return list(self.execute(*args, **kwargs) or [])
    
    def getSignature(self):
        return self.__class__.__name__

"""
list hace que el generador se resuelva completamente antes de retornar,
por lo que aun se puede retornar algun valor necesario. Si la ultima
capa propaga un resultado, este sera retornado por run().

run es el metodo a llamar cuando es la ultima capa y se quiere ejecutar
la cadena de decoradores. Si una capa llama otra capa internamente,
esta debe usar execute() para no resolver el generador prematuramente.
"""