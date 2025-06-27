# ⏱️ Pomodoro Tracker (Tkinter GUI)

A simple Pomodoro Timer application built with Python and Tkinter. Designed to help you stay productive by working in focused intervals and taking regular breaks.

> **This project was developed by me for educational and learning purposes.**

---

## 🧠 What is the Pomodoro Technique?

The **Pomodoro Technique** is a time management method where you break work into 25-minute focused intervals (called "Pomodoros") followed by short breaks. This helps reduce mental fatigue and boosts productivity.

---

## 📸 Screenshot

![Pomodoro UI](assets/readme_images/pomodoro_gui.jpg)

---

## 🚀 Features

- 🖥️ **Modern GUI** using `tkinter`
- 🔔 **Audio notification** at the start and end of work sessions
- 📝 **Task entry field** to stay focused on one goal
- 🎨 Custom fonts and background design
- 🔁 **Start**, **Done**, and **Reset** buttons for control
- 🧠 Supports Pomodoro-style work/break cycles

---

## 🛠️ Technologies Used

- Python 3.x
- `tkinter` (standard with Python)
- `playsound` for audio playback
- Custom assets (images, fonts, sounds)

---

## 📂 Project Structure

```

pomodoro_app/
│
├── assets/
│   ├── images/
│   │   └── pomodoro_logo.png         
│   ├── readme_images/
│   │   └── pomodoro_gui.jpg          
│   └── sounds/
│       ├── success_sound_effect.mp3  
│       └── work_time_start.mp3       
│
├── configuration.py
├── main.py                 
├── timer.py                
├── ui_layout.py           
└── README.md

````

---

## ▶️ How to Run

1. **Clone the repository** or download the files:

```bash
git clone https://github.com/your-username/pomodoro-tracker.git
cd pomodoro-tracker
````

2. **Install dependencies:**

```bash
pip install playsound
```

> `tkinter` is usually included with Python by default. If not, you may need to install it manually depending on your OS.

> For Windows users, `playsound==1.2.2` is recommended for compatibility.

3. **Run the app:**

```bash
python main.py
```

---

## 🔊 Sound Not Playing?

* Ensure the following sound files exist:

  * `assets/sounds/success_sound_effect.mp3`
  * `assets/sounds/work_start_sound.mp3`
* Make sure your device is not muted and has media permissions enabled.
* On Linux/Mac, `playsound` may require additional libraries like `gstreamer`.

---

## 🙌 Acknowledgments

* Font: [Montserrat](https://fonts.google.com/specimen/Montserrat)
* Icons and design inspired by [Pomodoro Technique](https://sketchplanations.com/the-pomodoro-technique)

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome! Feel free to fork the repo and submit a pull request.