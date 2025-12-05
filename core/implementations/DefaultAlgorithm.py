from ..base.Algorithm import Algorithm

class DefaultAlgorithm(Algorithm):
    
    def execute(self, *args, **kwargs):
        if kwargs:
            print(f"Executing {self.getSignature()} with keyword arguments: {kwargs}")
            yield f"Processed with kwargs: {kwargs}"
        

"""
Modulo de prueba para entender el funcionamiento de DefaultAlgorithm.

Puedes decorar cualquier implementacion de Algorithm con Logger para obtener logs de su ejecucion.

todas las clases son basadas en Executor

"""
def test():
    from ..base.Logger import Logger
    algo = DefaultAlgorithm()
    logger = Logger(algo)
    logger.execute(**{
        'quantum': 4,
        'processes': [
            {'id': 1, 'pila': [6, 7, 7]},
            {'id': 2, 'pila': [5, 3, 2]},
            {'id': 3, 'pila': [8, 1]}
        ]
    })

if __name__ == "__main__":
    test()