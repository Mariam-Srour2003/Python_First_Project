import tkinter as tk
from ratebkanone import ratebkanone


class taka3od(tk.Frame):
    def __init__(self, window, Shorottaka3od, first):
        super().__init__(window)
        self.first = first
        self.window = window
        self.Shorottaka3od = Shorottaka3od
        self.ratebkanone_instance = ratebkanone(self.window, self.first, self.Shorottaka3od)
        self.ratebkanone_instance.pack()
        buttonok = tk.Button(self.window, text="calculate", command=self.ma3ashtaka3od, width=15, height=2, bg="black",
                             fg="white", font=("Arial", 10))
        buttonok.pack()

    def ma3ashtaka3od(self):
        ma3ash = 85 * self.ratebkanone_instance.ratebkanone/100
        label_message = tk.Label(self.window, text="معاش تقاعد " + str(ma3ash), font=("Arial", 14), fg="green")
        label_message.pack()
