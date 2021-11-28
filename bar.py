from tkinter import *
from tkinter import ttk
import time

root = Tk()
def step():
    my_progress['value'] += 20


my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length = 100, mode = 'determinate')

my_progress.grid(row=0, column=0)

button = Button(root, text="progress", command = step)
button.grid(row = 0, column = 1)
root.mainloop()