import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Neon Clock")
root.geometry("780x320")
root.resizable(False, False)
root.configure(bg="#0d0d1a")

frame = tk.Frame(root, bg="#0d0d1a")
frame.pack(expand=True)

clock_label = tk.Label(
    frame,
    text="",
    font=("Courier", 64, "bold"),
    bg="#0d0d1a",
    fg="#00ffea",
)
clock_label.pack(side="left", padx=(0, 4))

ampm_label = tk.Label(
    frame,
    text="",
    font=("Courier", 22, "bold"),
    bg="#0d0d1a",
    fg="#2affc8",
)
ampm_label.pack(side="left", anchor="s", pady=(0, 14))

separator = tk.Label(
    root,
    text="─" * 44,
    bg="#0d0d1a",
    fg="#1a3a3a",
    font=("Courier", 10),
)
separator.pack()

date_label = tk.Label(
    root,
    text="",
    font=("Courier", 15),
    bg="#0d0d1a",
    fg="#2affc8",
    pady=4,
)
date_label.pack()

status_label = tk.Label(
    root,
    text="◉  LIVE",
    font=("Courier", 11),
    bg="#0d0d1a",
    fg="#0a5c4a",
    pady=2,
)
status_label.pack()

def update_time():
    time_string = strftime("%I:%M:%S")
    ampm_string = strftime("%p")
    date_string = strftime("%A,  %d  %B  %Y").upper()

    clock_label.config(text=time_string)
    ampm_label.config(text=ampm_string)
    date_label.config(text=date_string)

    if int(strftime("%S")) % 2 == 0:
        clock_label.config(fg="#00ffea")
    else:
        clock_label.config(fg="#006655")

    root.after(500, update_time)

update_time()
root.mainloop()