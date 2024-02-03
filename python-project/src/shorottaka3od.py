import tkinter as tk
from taka3od import taka3od

class Shorottaka3od(tk.Frame):
    def __init__(self, window, first):
        super().__init__(window)
        self.window = window
        self.first = first
        if first.age >= 55 and first.nbofworkyears >= 30:
            taka3od_instance = taka3od(self.window, self, self.first)  
            taka3od_instance.pack()
        else:
            label_message = tk.Label(self.window, text="شروط غير متوفرة لا يمكن طلب معاش تقاعد", font=("Arial", 14), fg="red")
            label_message.pack()
