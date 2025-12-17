from core.base.Logger import Logger
from core.implementations.PO.PollLog import PollLog

class PollingLogger(Logger):
    
    def log(self, message: str):
        return PollLog(f"[LOG]: {message}")