import tkinter as tk 
from tkinter import *
from tkinter import ttk
from typing import Counter
from timeit import default_timer as timer
from tkmacosx import Button
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = tk.Tk()

#create title label
myLabel1 = Label(root, text="   GROCERY STORE DEMO")
myLabel1.config(font = ('Helvetica', "20", "bold"))
myLabel1.grid(row=0, column=0)


#create list to keep track in and out flow time
times = []

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
        capacity_bar['value']+=10
        myLabel3 = Label(root, text = "Total people in store: "+str(count))
        myLabel3.config(font = ('Helvetica', 20))
        myLabel3.grid(column=0, row=3)
    else:
        global start
        start = timer()

    #increase capacity bar

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
        capacity_bar['value']+= (-10)
        myLabel3 = Label(root, text = "Total people in store: "+str(count))
        myLabel3.config(font = ('Helvetica', 20))
        myLabel3.grid(column=0, row=3)
    elif waitlist > 0:
        waitlist -= 1
        myLabel4 = Label(root, text = "Total people waiting: "+str(waitlist))
        myLabel4.config(font = ('Helvetica', 20))
        myLabel4.grid(column=0, row=5)
        global end
        end = timer()

    #check capcaity value

        waitTime = end-start 
        times.append(waitTime)
        avgWaitTime = int(sum(times)/len(times))

    if waitlist > 0:
        waitTimeLabel = Label(root, text = "estimated wait time is: "+ str(avgWaitTime)+" secs")
        waitTimeLabel.grid(column = 0, row = 6)

    #high risk label if capacity is >= 70%
    if capacity_bar['value'] >= 70:
        warningLabel = Label(root, text="high risk!!")
    else:
        warningLabel = Label (root, text = '                ')

    #put onto screen

    warningLabel.grid(column=0, row=4)


    myLabel3.grid(column=0, row=3)

def waitClick():
    global count
    global waitlist
    if 0 < count >= cap:
        waitlist += 1
        myLabel4 = Label(root,text = "Total people waiting: "+str(waitlist))
        myLabel4.config(font = ('Helvatical bold', 20))
        myLabel4.grid(column=0, row=5)
enterButton = Button(root, text = "enter", padx=50, pady=10, bg = "#5cd65c", command = enterClick)
enterButton.grid(row=1,column=0)

exitButton = Button(root, text="exit", padx = 50, pady = 10, bg = "#cc4400", command = exitClick)
exitButton.grid(row=1, column=1)

blankLabel = Label(root, text="                           ")
blankLabel.grid(row=1, column=2)

waitButton = Button(root,text = "wait", padx = 50, pady = 10, command = waitClick)
waitButton.grid(row=1,column=3)


#graphs
data2 = {'Day of Week': ["Sun","Mon","Tues","Weds","Thurs","Fri","Sat"],
        'Customers per day': ["504","316","376","385","352","398","477"]}
df2 = pd.DataFrame(data2,columns=['Day of Week','Customers per day'])

x1 = ["0", "9am","10am","11am","12pm","1pm","2pm","3pm","4pm","5pm","6pm"]
y1 = ["0", "13","25","35","50","58","42","55","20","35","65"]
fig1 = plt.figure(figsize=(4, 5))
plt.bar(x=x1, height=y1)
plt.xticks(x1, rotation=90)
plt.title("Friday: Customers per Hour")
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.draw()
canvas1.get_tk_widget().grid(row=9, column=0, ipadx=1, ipady=1)

x2 = ["Sun","Mon","Tues","Weds","Thurs","Fri","Sat"]
y2 = [504,316,376,385,352,398,477]
fig2 = plt.figure(figsize=(4, 5))
plt.plot(x2, y2)
plt.xticks(x2, rotation=90)
plt.title("Customers per Day")
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.draw()
canvas2.get_tk_widget().grid(row=9, column=1, ipadx=1, ipady=1)


root.mainloop()