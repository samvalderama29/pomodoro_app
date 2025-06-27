from tkinter import Tk
from timer import Timer
from ui_layout import PomodoroUI

root = Tk()

def update_timer_display(time_str):
    ui.update_display(time_str)

def session_started():
    ui.session_complete()

timer = Timer(update_timer_display, session_started)
ui = PomodoroUI(root, timer)

root.mainloop()