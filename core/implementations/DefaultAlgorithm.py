from ..base.Algorithm import Algorithm
from core.implementations.PO.Log import Log
from core.implementations.PO.Timestamp import Timestamp, TimestampState

from time import sleep, time
from random import randint
class DefaultAlgorithm(Algorithm):
    
    def execute(self, *args, **kwargs):
        test_logs = [
            'Loading resources...',
            'Processing data...',
            'Looping execution...',
            'Error',
            'Finding the 100 digits of pi...'
        ]
        exec_time = randint(5, 17)
        epoch = randint(1, 5) / 10
        start_time = time()
        yield Timestamp(TimestampState.START)
        while time() - start_time < exec_time:
            sleep(epoch)
            yield Log(test_logs[randint(0, len(test_logs)) - 1] )
            sleep(epoch)
            yield Timestamp(TimestampState.PAUSE)
            # pause work
            sleep(epoch)
            yield Timestamp(TimestampState.RESUME)
            # do some work
            sleep(epoch)
        yield Timestamp(TimestampState.END)

"""
Modulo de prueba para entender el funcionamiento de DefaultAlgorithm.

Puedes decorar cualquier implementacion de Algorithm con Logger para obtener logs de su ejecucion.

todas las clases son basadas en Executor

Cambios nuevos:

    1. Implementacion de parameter object concreta (Ver Log y Timestamp)
    2. Decoracion por capas (Ver estructura en main.py)
    3. Monitoreo constante (Ver decoradores)

Como funciona:

    La funcionalidad de generadores de python ayuda a mejorar esta implementacion
    ya que los generadores "Lazy" son iterables, por lo que podemos iterar infinitamente
    y obtener resultados en tiempo real sin utilizar un codigo complejo.

    Para implementar esto sin los generadores, necesitariamos un elemento concreto a traves
    el cual pueden pedir datos los distintos decoradores del tipo callback o una pila.

Como podemos utilizar esto para el proyecto:

    Si nuestro DefaultAlgorithm es un algoritmo de planificacion, podemos consumir los
    datos iniciales hasta que la pila de procesos se acabe. Ya que tenemos esta funcionalidad
    unidireccional, podemos implementar N capas donde cada capa tenga un proposito, y cada capa
    deje "pasar" valores destinados a otras capas.

    De esta forma, el algoritmo no debe tener mucha complicacion, solo retornar elementos especificos
    a conveniencia, y dada una buena implementacion de las capas, el resto del trabajo como mediciones
    y logs se haran automaticamente. Si queremos un componente grafico, podriamos progamar una capa 
    con esa responsabilidad, etc.

"""
