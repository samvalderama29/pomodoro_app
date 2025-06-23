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

    def start(self):
        if not self.running:
            self.running = True
            self.reps += 1
            self.thread = threading.Thread(target = self.run_timer)
            self.thread.start()

    def run_timer(self):
        if self.reps % 8 == 0:
            seconds = long_break_min * 60
        elif self.reps % 2 == 0:
            seconds = short_break_min * 60
        else:
            seconds = work_min * 60

        while seconds > 0 and self.running:
            mins, secs = divmod(seconds, 60)
            self.on_update(f"{mins:02}:{secs:02}")
            time.sleep(1)
            seconds -= 1

        if self.running:
            self.on_session_complete()

    def reset(self):
        self.running = False
        self.reps = 0
        self.on_update("00:00")