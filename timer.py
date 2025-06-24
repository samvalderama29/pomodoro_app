import time
import threading
from configurations import work_min, short_break_min, long_break_min
from playsound import playsound

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
            session_type = "break"
        elif self.reps % 2 == 0:
            seconds = short_break_min * 60
            session_type = "break"
        else:
            seconds = work_min * 60
            session_type = "work"

        if session_type == "work":
            threading.Thread(
                target=playsound,
                args = ("assets/sounds/work_time_start.mp3",),
                daemon = True
            ).start()
            time.sleep(4)

        end_time = time.time() + seconds

        while self.running and time.time() < end_time:
            remaining = int(end_time - time.time())
            mins, secs = divmod(remaining, 60)
            self.on_update(f"{mins:02}:{secs:02}")
            time.sleep(1)

        if self.running:
            self.on_session_complete()
            threading.Thread(
                target=playsound,
                args =("assets/sounds/success_sound_effect.mp3",),
                daemon =True
            ).start()

    def reset(self):
        self.running = False
        self.reps = 0
        self.on_update("25:00")

        if self.thread and self.thread.is_alive():
            self.thread.join()

    def done(self):
        self.running = False
        self.reps = 0
        threading.Thread(
            target = playsound,
            args = ("assets/sounds/success_sound_effect.mp3",),
            daemon = True
        ).start()