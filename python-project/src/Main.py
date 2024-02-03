import tkinter as tk
from tkinter import messagebox
import datetime
from first import First
from shorotta3wed import Shorotta3wed

if __name__ == "__main__":
    window = tk.Tk()
    window.title("User Information")
    window.geometry("1000x1500")
    first_instance = First(window)
    window.mainloop()
