from tkinter import *
from tkinter import ttk
import time
from typing import Counter
from timeit import default_timer as timer

root = Tk()

times = []

#create title label
myLabel1 = Label(root, text="         Grocery Store")
myLabel2 = Label(root, text="test")
myLabel1.config(font = ('Helvatical bold', 20))

myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=0)

#create capacity bar
capacity_bar = ttk.Progressbar(root, orient=HORIZONTAL, length = 100, mode = 'determinate')
capacity_bar.grid(row = 4, column = 2)

count = 0
waitlist = 0
cap = 10 #capacity(for creating waiting list)

def enterClick():
    global count
    global myLabel3
    global waitlist
    #count how many people in store
    if count < cap:
        count = count+1
        myLabel3 = Label(root, text = "Total people in store: "+str(count))
        myLabel3.config(font = ('Helvatical bold', 20))
        myLabel3.grid(column=0, row=3)
    else:
        waitlist += 1
        myLabel4 = Label(root, text = "Total people waiting: "+str(waitlist))
        myLabel4.config(font = ('Helvatical bold', 20))
        myLabel4.grid(column=0, row=5)
        global start
        start = timer()
    
    #increase capacity bar
    capacity_bar['value']+=10
    
    #high risk label if capacity is >= 70%
    if capacity_bar['value'] >= 70:
        warningLabel = Label(root, text="high risk!!")
    else:
        warningLabel = Label (root, text = '                ')
    
    
    #put everything onto screen
    warningLabel.grid(column=0, row=4)

def exitClick():
    global count
    global myLabel3
    global waitlist
    
    #decrease count
    if 0 < count <= cap and waitlist == 0:
        count = count-1
        myLabel3 = Label(root, text = "Total people in store: "+str(count))
        myLabel3.config(font = ('Helvatical bold', 20))
        myLabel3.grid(column=0, row=3)
    elif waitlist > 0:
        waitlist -= 1
        myLabel4 = Label(root, text = "Total people waiting: "+str(waitlist))
        myLabel4.config(font = ('Helvatical bold', 20))
        myLabel4.grid(column=0, row=5)
        global end
        end = timer()

        waitTime = end-start 
        times.append(waitTime)
        avgWaitTime = int(sum(times)/len(times))

        if waitlist > 0:
            waitTimeLabel = Label(root, text = "estimated wait-time is: "+ str(avgWaitTime)+" secs")
            waitTimeLabel.grid(column = 0, row = 6)
    
    
    
    #check capcaity value
    capacity_bar['value']+= (-10)
    
    #high risk label if capacity is >= 70%
    if capacity_bar['value'] >= 70:
        warningLabel = Label(root, text="high risk!!")
    else:
        warningLabel = Label (root, text = '                ')        
    
    #put onto screen
    
    warningLabel.grid(column=0, row=4)
    
    
    myLabel3.grid(column=0, row=3)



enterButton = Button(root, text = "enter", padx=50, pady=10, command = enterClick)
enterButton.grid(row=1,column=1)

exitButton = Button(root,text="exit", padx = 50, pady = 10, command = exitClick)
exitButton.grid(row=1, column=2)
root.mainloop() 