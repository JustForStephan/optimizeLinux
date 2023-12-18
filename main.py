import tkinter
from tkinter import *
import subprocess
from os import system

class update_widget():

    label = Label (text = "System aktualisieren")
    button1 = Button(text = "Nach Aktualisierungen suchen")
    button2 = Button(text = "Mögliche Aktualisierungen installieren")
    button3 = Button(text = "Pakete herunterladen und installieren")

    window_elements = [label, button1, button2, button3]
    def show(self):
        for element in self.window_elements:
            element.pack()
        window = tkinter.Tk()
        window.geometry("1000x1000")
        window.mainloop()

class main_widget():


    label = Label(text = "Willkommen beim Linux_Optimizer")
    button1 = Button ( text = "Aktualisiere dein System")
    button2 = Button (text = "Erneuere deinen App-Speicher")
    button3 = Button (text = "Mach doch was zu willst")


    window_elements = [label, button1, button2, button3]

    def show(self):
        for element in self.window_elements:
            element.pack()
        window = tkinter.Tk()
        window.geometry("1000x1000")
        window.mainloop()


# start of algorithm
main = main_widget()
main.show()