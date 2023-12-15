from tkinter import *
import subprocess
from tkinter import messagebox
from os import system

class Main_Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.logIn()
        self.windowBody()

    def windowBody(self):
        Button(self, text = "Führe eine Systemaktualisierung durch", command = self.open_sub_window())

    def open_sub_window(self):
        update_root = Tk()
        update_root.title = "Systemaktualierung"
        sub_Window(update_root)
        update_root.mainloop()

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

class sub_Window(Frame):
    def __init__(self):
        self.body_window()

    def body_window(self):
        label = Label(Frame, text = "Dein System wird aktualisiert, dies kann einige Zeit in Anspruch nehmen")



root = Tk()
root.geometry("300x200")
root.title("Linux Optimization Algorithm")
app = Main_Window(root)
root.mainloop()