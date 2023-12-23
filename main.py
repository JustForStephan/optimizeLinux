import tkinter as tk
import subprocess
import os

class update_widget():

    def update_sys(self):
        os.system("apt update")
        os.system("apt upgrade -y")
        os.system("apt clean")
        os.system("apt autoremove -y")

    def __init__(self):
        root_update = tk.Tk()
        root_update.title("Systemaktualisierung")
        label1 = tk.Label(root_update, text = "Mit der folgenden Anwendung wird folgendes am System ausgeführt:")
        label2 = tk.Label(root_update, text = "   1. Neue Aktualisierungen werden gesucht und installiert.")
        label3 = tk.Label(root_update, text = "   2. Der Aktualisierungschache wird geleert.")
        label4 = tk.Label(root_update, text = "   3. Alle überflüssigen Pakete werden aus dem System gelöscht.")
        button_dec = tk.Button(root_update, text = "Ich möchte eine vollständige Systemaktualisierung durchführen", command = lambda: self.update_sys())
        window_labels = [label1, label2, label3, label4, button_dec]
        for i in window_labels:
            i.pack()
        root_update.mainloop()


class Restart_wlan():
    clicked = False
    def restart(self):
        os.system("sudo /etc/init.d/networking restart")
        self.clicked = True
    def __init__(self):
        root_wlan = tk.Tk()
        root_wlan.title("Neustart des WLANs")
        label1 = tk.Label(root_wlan, text = "Wollen Sie das WLAN neustarten?")
        button = tk.Button(root_wlan, text = "Ja", command = lambda: self.restart())
        window_elements = [label1, button]
        for i in window_elements:
            i.pack()
        if (self.clicked == True):
            label2 = tk.Label(root_wlan, text = "Das WLAN wurde neugestartet!")
            label2.pack()
        root_wlan.mainloop()

class main_widget():

    def actualize_sys(self):
        update_widget()
    def restart_wlan(self):
       Restart_wlan()

    def __init__(self):
        root = tk.Tk()
        root.title("Linux_Optimizer")
        label = tk.Label(root, text="Willkommen beim Linux_Optimizer")
        button1 = tk.Button(root, text="Aktualisiere dein System", command = lambda: self.actualize_sys())
        button2 = tk.Button(root, text="Starte dein WLAN neu", command = lambda: self.restart_wlan())
        window_elements = [label, button1, button2]
        for i in window_elements:
            i.pack()
        root.mainloop()

# start of algorithm
app = main_widget()
