from tkinter import *
import subprocess
from tkinter import messagebox
from os import system

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.logIn()
        self.update_sys()

    def logIn(self):
        try:
            subprocess.check_call(["sudo", "-S", "apt", "install", "mc", "-y"])
        except subprocess.CalledProcessError:
            print("Failed")
        #    messagebox.askokcancel.showinfo("message", "OOOOPS...\nWrong password!")
        #else:
         #   messagebox.askokcancel.showinfo("message", "Login successful!")

    def update_sys(self):
        system("apt clear")
        system("apt update")
        system("apt upgrade")



root = Tk()
root.geometry("300x200")
root.title("Linux Optimization Algorithm")
app = Window(root)
root.mainloop()


