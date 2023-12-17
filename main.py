import tkinter
from tkinter import *
import subprocess
from tkinter import messagebox
from os import system

class Main_Window:
    def __init__(self, root):
        self.root = root
        #if (widget == "main_widget"):
        #    self.main_widget
        #if(widget == "update_widget"):
        #   self.update_widget

    def main_widget(self, root):
        return root.Label(text = "Willkommen bei OptiLin!")

    def update_widget(self):
        pass

def logIn():
    try:
        subprocess.check_call(["sudo", "-S", "apt", "install", "mc", "-y"])
    except subprocess.CalledProcessError:
        print("Failed")

def run_app(root, widget):
    #logIn()
    if(widget == "main_widget"):
        root.title("OptiLin")
        app =  Main_Window(root)
        app.main_widget(root)
    if (widget == "update_widget"):
        root.title("Aktualisierung des Systems")
        return Main_Window(root, "update_widget")

        #    messagebox.askokcancel.showinfo("message", "OOOOPS...\nWrong password!")
        # else:
        #   messagebox.askokcancel.showinfo("message", "Login successful!")

widget = "main_widget"
root = tkinter
root.geometry("300x200")
app = None
app = run_app(root, widget)
app.pack()
root.mainloop()
