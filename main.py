import tkinter as tk
from timer import Timer
from ui_layout import PomodoroUI

class PomodoroApp:
    def __init__(self):
        self.root = tk.Tk()
        self.timer = Timer(self.update_display, self.session_complete)
        self.ui = PomodoroUI(self.root, self.timer)

    def update_display(self, time_str):
        self.ui.update_display(time_str)

    def session_complete(self):
        self.ui.session_complete()

    def run(self):
        self.root.mainloop()