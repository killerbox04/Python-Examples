#Toggle Switch Testing

from textwrap import fill
from tkinter import *
import tkinter as ttk
from turtle import bgcolor, bgpic, color, left

global toggleButton

#def buttonToggle():
    #if buttontext = off
        #buttontext = on
        #buttoncolor = green
        #(return)?
    #elif buttontext = on
        #buttontext = off
        #buttoncolor = red  


def buttonToggle():
     global toggleButton
     if toggleButton.cget("text") == "OFF":
         toggleButton.config(bg = "Green")
         toggleButton.config(activebackground = "Green")
         toggleButton.config(text = "ON")
     elif toggleButton.cget("text") == "ON":
         toggleButton.config(bg = "Red")
         toggleButton.config(activebackground = "Red")
         toggleButton.config(text = "OFF")


root = ttk.Tk()
root.geometry = ("400x400")




toggleButton = ttk.Button(
    root,
    text = "OFF",
    width = 50,
    height = 10,
    command = lambda : buttonToggle(),
    bg = "red",
    fg = "white",
    activebackground = "red",
    activeforeground = "white"
)

toggleButton.pack()

root.mainloop()