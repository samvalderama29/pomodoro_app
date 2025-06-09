import time
import threading
from configurations import work_min, short_break_min, long_break_min

class Timer:
    def __init__(self, on_update, on_session_complete):
        self.on_update = on_update
        self.on_session_complete = on_session_complete
        self.reps = 0
        self.running = False
        self.thread = None
