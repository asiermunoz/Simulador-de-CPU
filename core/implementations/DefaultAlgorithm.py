from ..base.Algorithm import Algorithm

class DefaultAlgorithm(Algorithm):
    
    def execute(self, *args, **kwargs):
        if kwargs:
            yield f"DefaultAlgorithm executed with kwargs: {kwargs}"
            yield [99, 0, 8 ,7]
            yield [100]
        

"""
Modulo de prueba para entender el funcionamiento de DefaultAlgorithm.

Puedes decorar cualquier implementacion de Algorithm con Logger para obtener logs de su ejecucion.

todas las clases son basadas en Executor

"""
