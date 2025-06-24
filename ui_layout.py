import tkinter as tk
from tkinter import font

class PomodoroUI:
    def __init__(self, root, timer):
        self.root = root
        self.timer = timer

        self.setup_window()
        self.setup_fonts()
        self.setup_background()
        self.create_widgets()
        self.place_widgets()

    def setup_window(self):
        self.root.title("Pomodoro Trakcer")
        self.root.geometry("800x450")
        self.root.resizable(False, False)
        self.root.iconphoto(False, tk.PhotoImage(file = "pomodoro_logo.png"))

    def setup_fonts(self):
        display_font = "Montserrat" if "Montserrat" in font.families() else "Helvetica"
        self.primary_font = (display_font, 18)
        self.label_font = (display_font, 24, "bold")
        self.timer_font = (display_font, 83, "bold")
        self.button_font = (use_font, 12)