import tkinter as tk
from ta3wed import ta3wed


class Shorotta3wed(tk.Frame):
    def __init__(self, window, first):
        super().__init__(window)
        self.window = window
        self.first = first
        self.button_frame = None  # Add this line to initialize the button_frame attribute

        if first.age >= 64 or first.nbofworkyears >= 25:
            self.acceptedgonext()
        else:
            self.checkbox_frame = tk.Frame(self.window)
            self.checkbox_frame.pack()

            self.checkbox1_var = tk.IntVar()
            self.checkbox1 = tk.Checkbutton(
                self.checkbox_frame, text="مريض؟", variable=self.checkbox1_var)
            self.checkbox1.pack()

            self.checkbox2_var = tk.IntVar()
            self.checkbox2 = tk.Checkbutton(
                self.checkbox_frame, text="وفاة؟", variable=self.checkbox2_var)
            self.checkbox2.pack()

            if str(first.gender_var.get()) == "female":
                self.checkbox3_var = tk.IntVar()
                self.checkbox3 = tk.Checkbutton(
                    self.checkbox_frame, text="زواج؟", variable=self.checkbox3_var)
                self.checkbox3.pack()

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        choosed = tk.Button(self.button_frame, text="DONE", command=self.clickDone, width=15, height=2, bg="black",
                            fg="white", font=("Arial", 10))
        choosed.grid(row=0, column=0, padx=10)

    def clickDone(self):
        if self.checkbox1_var.get() or self.checkbox2_var.get():
            self.acceptedgonext()
        elif str(self.first.gender_var.get()) == "female":
            if self.checkbox3_var.get():
                self.acceptedgonext()
            else:
                if self.button_frame:
                   self.button_frame.destroy()
                label_message = tk.Label(self.window, text="شروط غير متوفرة لا يمكن طلب تعويض", font=("Arial", 14),
                                         fg="red")
                label_message.pack()
        else:
            if self.button_frame:
                self.button_frame.destroy()
            label_message = tk.Label(self.window, text="شروط غير متوفرة لا يمكن طلب تعويض", font=("Arial", 14),
                                     fg="red")
            label_message.pack()

    def acceptedgonext(self):
        if self.button_frame:
            self.button_frame.destroy()
        ta3wed_instance = ta3wed(self.window, self, self.first)
        ta3wed_instance.pack()
