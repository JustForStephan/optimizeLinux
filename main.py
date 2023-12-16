from tkinter import *
import subprocess
from tkinter import messagebox
from os import system

class Main_Window(Frame):
    def __init__(self, master=None, widget):
        Frame.__init__(self, master)
        self.widget = widget
        self.master = master
        self.logIn()
        if (widget == "main_widget"):
            self.main_widget
        if(widget == "update_widget"):
            self.update_widget

    def main_widget(self):
        pass
    def update_widget(self):
        pass

widget = "main_widget"
root = Tk()
root.geometry("300x200")
def run_app(root, widget):
    login = logIn()
    if(widget == "main_widget"):
        root.title("Linux Optimization Algorithm")
        app = Main_Window(root, "main_widget")
    if (widget == "update_widget"):
        root.title("Aktualisierung des Systems")
        app = Main_Window(root, "update_widget")

    def logIn():
        try:
            subprocess.check_call(["sudo", "-S", "apt", "install", "mc", "-y"])
        except subprocess.CalledProcessError:
            print("Failed")
        #    messagebox.askokcancel.showinfo("message", "OOOOPS...\nWrong password!")
        # else:
        #   messagebox.askokcancel.showinfo("message", "Login successful!")
root.mainloop()