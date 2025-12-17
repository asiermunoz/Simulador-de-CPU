from ..base.Recorder import Recorder
from time import time

class ConcreteTimeRecorder(Recorder):
    def __init__(self, decoratee = None):
        super().__init__(decoratee)
        self.recorded_data = []
        self.start_time = None

    def processData(self, data):
        if not self.start_time:
            self.start_time = time()

        measurement = (time() - self.start_time, str(data))
        self.recorded_data.append(measurement)
