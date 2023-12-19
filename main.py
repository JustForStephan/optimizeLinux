import tkinter as tk
from tkinter import ttk

''''''
class update_widget():

    def __init__(self):

        label = tk.Label (text = "System aktualisieren")
        button1 = tk.Button(text = "Nach Aktualisierungen suchen")
        button2 = tk.Button(text = "Mögliche Aktualisierungen installieren")
        button3 = tk.Button(text = "Pakete herunterladen und installieren")

        window_elements = [label, button1, button2, button3]
    def show(self):
        for element in self.window_elements:
            element.pack()
        window = tk.Tk()
        window.title("Hello from the dark side")
        window.geometry("1000x1000")
        window.mainloop()

class another_widget:
    pass

class main_widget():

    def __init__(self):

        root = tk.Tk()
        root.title("Hello")
        label = tk.Label(root, text="Willkommen beim Linux_Optimizer")
        button1 = tk.Button(root, text="Aktualisiere dein System")
        button2 = tk.Button(root, text="Erneuere deinen App-Speicher")
        button3 = tk.Button(root, text="Mach doch was zu willst")
        window_elements = [label, button1, button2, button3]
        for i in window_elements:
            i.pack()
        root.mainloop()



# start of algorithm
app = main_widget()
