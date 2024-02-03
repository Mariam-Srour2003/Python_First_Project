from ratebkanone import ratebkanone
import tkinter as tk


class ta3wed(tk.Frame):
    def __init__(self, window, Shorotta3wed, first):
        super().__init__(window)
        self.first = first
        self.window = window
        self.Shorotta3wed = Shorotta3wed
        self.ratebkanone_instance = ratebkanone(
            self.window, self.first, self.Shorotta3wed)
        self.ratebkanone_instance.pack()
