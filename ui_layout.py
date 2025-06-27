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
        self.root.title("Pomodoro Tracker")
        self.root.geometry("800x450")
        self.root.resizable(False, False)
        self.root.iconphoto(False, tk.PhotoImage(file ="assets/images/pomodoro_logo.png"))

    def setup_fonts(self):
        display_font = "Montserrat" if "Montserrat" in font.families() else "Helvetica"
        self.primary_font = (display_font, 15)
        self.label_font = (display_font, 24, "bold")
        self.timer_font = (display_font, 83, "bold")
        self.button_font = (display_font, 12)

    def setup_background(self):
        self.bg_photo = tk.PhotoImage(file ="assets/images/pomodoro_window.png")
        self.bg_label = tk.Label(self.root, image = self.bg_photo)
        self.bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    def create_widgets(self):
        self.task_entry = tk.Entry(self.root, font = self.primary_font, width = 40, justify = "center", bd = 1.5)
        self.task_entry.insert(0, "Enter the task you want to finish")

        self.label = tk.Label(self.root, text = "TIMER", font = self.label_font, bg = "#d6a254", fg = "#000000", bd = 0)

        self.time_display = tk.Label(self.root, text = "25:00", font = self.timer_font, bg = "#d6a254", fg = "#000000", bd = 0)

        self.start_button = tk.Button(self.root, text = "START", command = self.start_timer, font = self.button_font,
                                      fg = "white", bg = "#093FBA", width = 8, relief = "flat")
        self.done_button = tk.Button(self.root, text = "DONE", command = self.done_button_clicked, font = self.button_font,
                                      fg = "white", bg = "#06923E", width = 8, relief = "flat")
        self.reset_button = tk.Button(self.root, text = "RESET", command = self.full_reset, font = self.button_font,
                                      fg = "white", bg = "#8A0000", width = 8, relief = "flat")

    def place_widgets(self):
        self.task_entry.place(relx = 0.5, rely = 0.38, anchor = "center")
        self.label.place(relx = 0.5, rely = 0.47, anchor = "center")
        self.time_display.place(relx = 0.5, rely = 0.67, anchor = "center")
        self.start_button.place(relx = 0.35, rely = 0.87, anchor = "center")
        self.done_button.place(relx = 0.5, rely = 0.87, anchor = "center")
        self.reset_button.place(relx = 0.65, rely = 0.87, anchor = "center")

    def start_timer(self):
        self.timer.start()

    def update_display(self, time_str):
        self.time_display.config(text = time_str)

    def session_complete(self):
        mode = "BREAK TIME!" if self.timer.reps % 2 == 0 else "WORK TIME!"
        self.label.config(text = mode)

    def full_reset(self):
        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, "Enter the task you want to finish")
        self.time_display.config(text = "25:00")
        self.label.config(text = "TIMER")
        self.timer.reset()

    def done_button_clicked(self):
        self.timer.done()
        self.full_reset()