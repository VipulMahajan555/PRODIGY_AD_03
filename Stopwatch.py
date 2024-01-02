import tkinter as tk
import time

def start_stopwatch():
    global running, start_time, elapsed_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        start_button.config(text="STOP")
        update()
    else:
        running = False
        start_button.config(text="START")
        update()

def reset_stopwatch():
    global elapsed_time, running
    running = False
    start_button.config(text="START")
    elapsed_time = 0
    label.config(text="00:00:00.000", font=("Arial Bold", 20), fg="black")

def update():
    global elapsed_time
    if running:
        elapsed_time = time.time() - start_time

    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)

    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
    label.config(text=time_str)
    window.after(10, update)

window = tk.Tk()
window.title("STOPWATCH")
window.configure(bg="black")
label = tk.Label(window, text="YOUR PERSONAL STOPWATCH", font=("Arial Bold", 50), bg="black", fg="pink")
label.pack()

window.geometry('350x350')

running = False
elapsed_time = 0
start_time = 0  # Initialize start_time variable

label = tk.Label(window, text="00:00:00.000", font=("Arial", 100))
label.pack(pady=20)

start_button = tk.Button(window, text="START", font=("Arial Bold", 15), width=50, bg="pink", fg="black", command=start_stopwatch)
start_button.pack(padx=10, pady=5, side=tk.LEFT)

reset_button = tk.Button(window, text="RESET", font=("Arial Bold", 15), width=50, bg="pink", fg="black", command=reset_stopwatch)
reset_button.pack(padx=10, pady=5, side=tk.RIGHT)

window.mainloop()
