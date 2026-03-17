import tkinter as tk
from time import strftime

# tkinter is the library that creates gui based application. above we rename it as tk so its easy for use .
# strftime reads the current time from our computer and formats it as text

# create the window
root = tk.Tk()
root.title("Modern clock")
root.geometry("780x320")
root.resizable(False, False)
root.configure(bg="#0d0d1a")

"""
tk.Tk() create the main window or ui and everyting goes inside it. 
.title() set the name in the title bar. .geometry() set the size->width x height in pixels.
.resizable(height=False,width=False) lock the size so that the use cannot stretch it .
.configure(bg=) sets the background color using a hex color code

"""

# creating a frame
frame = tk.Frame(root, bg="#0d0d1a")
frame.pack(expand=True)

#  frame is an box inside the window. here we put the time and am/pm labes inside it . expand= true  centers the text or what written inside it in the window

# writing time and am/pm labels
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


"""
tk.Label create a text widget, text sstart with empty string. it will fill the time lateer. 
font is taking three things,1:font name,2:font size, font weight
bg is background color, fg is text color 
side = left palce both lables next to each other horizontally
anchor ="s" pin am/pm  equall in bottom .
pady(0,14) lift it slightly either up or down """

separator = tk.Label(
    root,
    text="--" * 44,
    bg="#0d0d1a",
    fg="#1a3a3a",
    font=("Courier", 10)
)
separator.pack()

date_label = tk.Label(
    root,
    text="",
    font=("Courier", 15),
    bg="#0d0d1a",
    fg="#2affcd",
    pady=4,
)
date_label.pack()
root.mainloop()
