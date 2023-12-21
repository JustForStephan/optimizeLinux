import tkinter as tk
from tkinter import ttk

''''''
class update_widget():

    def __init__(self):
        root_update = tk.Tk()
        root_update.title("Systemaktualisierung")
        label1 = tk.Label(root_update, text = "Mit der folgenden Anwendung wird folgendes am System ausgeführt:")
        label2 = tk.Label(root_update, text = "   1. Neue Aktualisierungen werden gesucht und installiert.")
        label3 = tk.Label(root_update, text = "   2. Der Aktualisierungschache wird geleert.")
        label4 = tk.Label(root_update, text = "   3. Alle überflüssigen Pakete werden aus dem System gelöscht.")
        label5 = tk.Label(root_update, text = "Möchten Sie eine vollständige Systemaktualisierung durchführen?", bg='#fff')
        window_labels = [label1, label2, label3, label4, label5]
        for i in window_labels:
            i.pack()
        root_update.mainloop()


class another_widget:
    pass



class main_widget():

    def actualize_sys(self):
        main_widget()

    def __init__(self):

        root = tk.Tk()
        root.title("Linux_Optimizer")
        label = tk.Label(root, text="Willkommen beim Linux_Optimizer")
        button1 = tk.Button(root, text="Aktualisiere dein System", command = self.actualize_sys())
        button2 = tk.Button(root, text="Erneuere deinen App-Speicher")
        button3 = tk.Button(root, text="Mach doch was zu willst")
        window_elements = [label, button1, button2, button3]
        for i in window_elements:
            i.pack()
        root.mainloop()

# start of algorithm
app = main_widget()
