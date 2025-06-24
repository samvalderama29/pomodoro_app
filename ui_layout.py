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
