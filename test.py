from tkinter import *
from typing import Counter
from timeit import default_timer as timer


root = Tk()


myLabel1 = Label(root, text="         Grocery Store")
myLabel2 = Label(root, text="test")
myLabel1.config(font = ('Helvatical bold', 20))

myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)

count = 0
waitlist = 0
cap = 10 #capacity

def enterClick():
    global count
    global waitlist
    if count < cap:
        count = count+1
        myLabel3 = Label(root, text = "Total people in store: "+str(count))
        myLabel3.config(font = ('Helvatical bold', 20))
        myLabel3.grid(column=0, row=3)
    else:
        waitlist += 1
        myLabel4 = Label(root, text = "Total people waiting: "+str(waitlist))
        myLabel4.config(font = ('Helvatical bold', 20))
        myLabel4.grid(column=0, row=4)

def exitClick():
    global count
    global waitlist
    if 0 < count <= cap and waitlist == 0:
        count = count-1
        myLabel3 = Label(root, text = "Total people in store: "+str(count))
        myLabel3.config(font = ('Helvatical bold', 20))
        myLabel3.grid(column=0, row=3)
    elif waitlist > 0:
        waitlist -= 1
        myLabel4 = Label(root, text = "Total people waiting: "+str(waitlist))
        myLabel4.config(font = ('Helvatical bold', 20))
        myLabel4.grid(column=0, row=4)

enterButton = Button(root, text = "enter", padx=50, pady=10, command = enterClick)
enterButton.grid(row=1,column=1)

exitButton = Button(root,text="exit", padx = 50, pady = 10, command = exitClick)
exitButton.grid(row=1, column=2)

root.mainloop()