import tkinter
from tkinter import *
import subprocess
from tkinter import messagebox
from os import system

class main_widget():

    window = Tk()
    window.geometry("300x200")
    label = Label(window, text = "Willkommen beim Linux_Optimizer")
    button1 = Button (window, text = "Aktualisiere dein System")
    button2 = Button (window, text = "Erneuere deinen App-Speicher")
    button3 = Button (window, text = "Mach doch was zu willst")

    widgets = [main_widget]
    window_elements = [label, button1, button2, button3]
    for element in window_elements:
        element.pack()
    window.mainloop()

# start of algorithm
main = main_widget()