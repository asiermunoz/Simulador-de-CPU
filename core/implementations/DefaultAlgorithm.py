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
            yield Log(f"Executing... {test_logs[randint(0, len(test_logs)) - 1]}")
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

"""
