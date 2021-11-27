from tkinter import *
from typing import Counter


root = Tk()


myLabel1 = Label(root, text="Grocery Store")
myLabel2 = Label(root, text="test")


myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

count = 0

def enterClick():
    global count
    count = count+1
    myLabel3 = Label(root, text = count)
    myLabel3.grid(column=2, row=1)

def exitClick():
    global count
    count = count-1
    myLabel3 = Label(root, text = count)
    myLabel3.grid(column=2, row=1)

enterButton = Button(root, text = "enter", padx=50, pady=10, command = enterClick)
enterButton.grid(row=0,column=2)

exitButton = Button(root,text="exit", padx = 50, pady = 10, command = exitClick)
exitButton.grid(row=0, column=3)
root.mainloop() 