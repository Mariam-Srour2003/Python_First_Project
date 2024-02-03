import tkinter as tk
from tkinter import messagebox
import datetime
from shorotta3wed import Shorotta3wed
from shorottaka3od import Shorottaka3od


class First(tk.Frame):
    age = 0
    nbofworkyears = 0
    gender_var = "male"
    dsw = 0
    dew = 0
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.window.title("User Information")
        self.window.geometry("500x500")

        label_name = tk.Label(self.window, text="الاسم الثلاثي:", font=("Arial", 15, "bold"))
        label_name.pack()
        self.entry_name = tk.Entry(self.window, font=("Arial", 12))
        self.entry_name.pack()

        label_dob = tk.Label(self.window, text="(YYYY-MM-DD)تاريخ الولاده", font=("Arial", 15, "bold"))
        label_dob.pack()
        self.entry_dob = tk.Entry(self.window, font=("Arial", 12))
        self.entry_dob.pack()

        label_dsw = tk.Label(self.window, text="(YYYY-MM-DD)تاريخ بدء العمل", font=("Arial", 15, "bold"))
        label_dsw.pack()
        self.entry_dsw = tk.Entry(self.window, font=("Arial", 12))
        self.entry_dsw.pack()

        label_dew = tk.Label(self.window, text="(YYYY-MM-DD)تاريخ انهاء العمل", font=("Arial", 15, "bold"))
        label_dew.pack()
        self.entry_dew = tk.Entry(self.window, font=("Arial", 12))
        self.entry_dew.pack()

        tk.Label(self.window, text="الجنس", font=("Arial", 15, "bold")).pack()
        self.gender_var = tk.StringVar(value="male")
        gender_frame = tk.Frame(self.window)
        gender_frame.pack()

        male_radio = tk.Radiobutton(gender_frame, text="ذكر", variable=self.gender_var, value="male")
        male_radio.grid(row=0, column=0)

        female_radio = tk.Radiobutton(gender_frame, text="أنثى", variable=self.gender_var, value="female")
        female_radio.grid(row=0, column=1)

        tk.Label(self.window, text="").pack()
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack()

        m3ashtaka3od = tk.Button(self.button_frame, text="معاش تقاعد", command=self.navigate_to_shorottaka3od, width=15, height=2, bg="black", fg="white", font=("Arial", 10))
        m3ashtaka3od.grid(row=0, column=0, padx=10)

        ta3wed = tk.Button(self.button_frame, text="تعويض", command=self.navigate_to_shorotta3wed, width=15, height=2, bg="black", fg="white", font=("Arial", 10))
        ta3wed.grid(row=0, column=1, padx=10)

    def calculate_age(self, date_of_birth):
        try:
            dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use the format YYYY-MM-DD.")
            return
        current_date = datetime.date.today()
        self.age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
        return self.age

    def calculate_nb_of_work_year(self, date_of_birth, datesw, dateew):
        try:
            dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
            self.dsw = datetime.datetime.strptime(datesw, "%Y-%m-%d").date()
            self.dew = datetime.datetime.strptime(dateew, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use the format YYYY-MM-DD.")
            return
        age_at_start = self.dsw.year - dob.year - ((self.dsw.month, self.dsw.day) < (dob.month, dob.day))
        age_at_end = self.dew.year - dob.year - ((self.dew.month, self.dew.day) < (dob.month, dob.day))
        age18 = dob + datetime.timedelta(days=18 * 365)
        age64 = dob + datetime.timedelta(days=64 * 365)
        if age_at_start < 18:
            self.dsw = age18
        elif age_at_end > 64:
            self.dew = age64
        self.nbofworkyears = self.dew.year - self.dsw.year
        return self.nbofworkyears

    def navigate_to_shorottaka3od(self):
        user_age = self.calculate_age(self.entry_dob.get())
        nbofworkedyears = self.calculate_nb_of_work_year(self.entry_dob.get(), self.entry_dsw.get(), self.entry_dew.get())
        print(user_age)
        print(nbofworkedyears)
        self.button_frame.destroy()  # Remove the buttons from the frame
        shorottaka3od_instance = Shorottaka3od(self.window, self)
        shorottaka3od_instance.pack()

    def navigate_to_shorotta3wed(self):
        user_age = self.calculate_age(self.entry_dob.get())
        nbofworkedyears = self.calculate_nb_of_work_year(self.entry_dob.get(), self.entry_dsw.get(), self.entry_dew.get())
        print(user_age)
        print(nbofworkedyears)

        self.button_frame.destroy()  # Remove the buttons from the frame
        shorotta3wed_instance = Shorotta3wed(self.window, self)
        shorotta3wed_instance.pack()


if __name__ == "__main__":
    window = tk.Tk()
    window.title("User Information")
    window.geometry("500x500")

    first_instance = First(window)
    window.mainloop()