import tkinter as tk


class ratebkanone(tk.Frame):
    nbofmonths = 0
    ratebkanone = 0
    ratebjaded2017 = [
        0,
        950000,
        985000,
        1020000,
        1055000,
        1090000,
        1125000,
        1165000,
        1205000,
        1245000,
        1285000,
        1325000,
        1375000,
        1425000,
        1475000,
        1525000,
        1575000,
        1635000,
        1695000,
        1755000,
        1815000,
        1875000,
        1945000,
        2015000,
        2085000,
        2155000,
        2225000,
        2305000,
        2385000,
        2465000,
        2545000,
        2625000,
        2720000,
        2815000,
        2910000,
        3005000,
        3100000,
        3215000,
        3330000,
        3445000,
        3560000,
        3675000,
        3805000,
        3935000,
        4065000,
        4195000,
        4325000,
        4475000,
        4625000,
        4775000,
        4925000,
        5075000,
        5245000
    ]

    def __init__(self, window, first, Shorot):
        self.window = window
        self.selected_option = tk.StringVar()
        self.first = first
        options = [
            "لا شهادة",
            "متوسط",
            "قسم ثاني",
            "بكالوريا فنية",
            "اجازة جامعية",
            "امتياز فني",
            "اجازة تعليمية",
            "شهاده الكفاءه"
        ]

        for option in options:
            rb = tk.Radiobutton(self.window, text=option,
                                variable=self.selected_option, value=option)
            rb.pack(anchor=tk.W)
        self.checkbox_state = tk.IntVar()
        checkbox = tk.Checkbutton(
            self.window, text="استاذ تعليم ثانوي؟", variable=self.checkbox_state)
        checkbox.pack()
        self.button = tk.Button(self.window, text="Get Selected Option", command=self.get_selected_option, width=15, height=2,
                                bg="black", fg="white", font=("Arial", 10))
        self.button.pack()
        self.window.mainloop()

    def get_selected_option(self):
        selected_option = self.selected_option.get()
        self.button.destroy()
        print("Selected Option:", selected_option)
        months = self.dependonnbofyears()
        index = int(self.e7tesabdarajetratebkanone())
        print(months)
        print(index)
        self.ratebkanone = months * self.ratebjaded2017[index]
        print(self.ratebkanone)
        label_message = tk.Label(self.window, text="راتب القانوني: " +
                                 str(self.ratebkanone), font=("Arial", 14), fg="green")
        label_message.pack()

    def dependonnbofyears(self):
        x = self.first.nbofworkyears
        y = 0
        if x > 30:
            y = y + (x - 30) * 3
            y = y + 20 * 2
            y = y + 10
        elif 30 >= x > 10:
            y = y + (x - 10) * 2
            y = y + 10
        elif x <= 10:
            y = y
        self.nbofmonths = y
        return y

    def e7tesabdarajetratebkanone(self):
        daraja = 0
        darajaestethna2eye = 0
        daraja = daraja + int(self.first.nbofworkyears / 2)  # kl sentan daraji
        getyear1 = str(self.first.dsw)
        getyear2 = str(self.first.dew)
        startyear = int(getyear1.split('-')[0])
        endyear = int(getyear2.split('-')[0])
        if startyear <= 1977:
            daraja = daraja + 1
            darajaestethna2eye = darajaestethna2eye + 1
            print(daraja, "بدء قبل ال 1978 فمن قانون 80 درجه: ")
        if startyear <= 1978:
            daraja = daraja + 2
            darajaestethna2eye = darajaestethna2eye + 2
            print(daraja, "بدء قبل ال 1979 فمن قانون 81 درجه: ")
        if startyear <= 2007:
            daraja = daraja + 6
            darajaestethna2eye = darajaestethna2eye + 6
            print(daraja, "بدء قبل ال 2008 فمن قانون 46 درجه: ")
        if self.checkbox_state.get() == 1:
            daraja = daraja + 6
            darajaestethna2eye = darajaestethna2eye + 6
            print(daraja, "استاذ تعليم ثانوي قانون 148 درجه: ")
        if self.checkbox_state.get() == 0:
            daraja = daraja + 3
            darajaestethna2eye = darajaestethna2eye + 3
            print(daraja, "ليس استاذ تعليم ثانوي قانون 244 درجه: ")
        if self.checkbox_state.get() == 0:
            daraja = daraja + 3
            darajaestethna2eye = darajaestethna2eye + 3
            print(daraja, "ليس استاذ تعليم ثانوي قانون 102 درجه: ")
        if self.checkbox_state.get() == 0:
            if startyear <= 2009:
                daraja = daraja + 4.5
                darajaestethna2eye = darajaestethna2eye + 4.5
                print(daraja, "ليس استاذ تعليم ثانوي بدء قبل ال 2010 قانون 223 درجه: ")
            if startyear >= 2010:
                daraja = daraja + 4
                darajaestethna2eye = darajaestethna2eye + 4
                print(daraja, "ليس استاذ تعليم ثانوي بدء بعد ال 2010 قانون 223 درجه ")
        if self.checkbox_state.get() == 1:
            daraja = daraja + 4
            darajaestethna2eye = darajaestethna2eye + 4
            print(daraja, "استاذ تعليم ثانوي قانون 159 درجه: ")
        if str(self.selected_option.get()) == "لا شهادة":
            daraja = darajaestethna2eye + \
                ((1996-startyear)/3)+((endyear-1996)/2)
            print(daraja, " لا يملك شهاده درجه")
        if str(self.selected_option.get()) == "متوسط":
            daraja = daraja
            print(daraja, " شهاده متوسط درجه")
        if str(self.selected_option.get()) == "قسم ثاني":
            if startyear == 1994 or startyear == 1995 or startyear == 1996:
                daraja = daraja + 1
                print(daraja, " شهاده قسم ثاني درجه")
        if str(self.selected_option.get()) == "بكالوريا فنية":
            daraja = daraja + 6
            print(daraja, " شهاده بكالوريا فنيه درجه")
        if str(self.selected_option.get()) == "اجازة جامعية":
            daraja = daraja + 6
            print(daraja, " اجازه جامعيه درجه")
        if str(self.selected_option.get()) == "امتياز فني":
            daraja = daraja + 11
            print(daraja, "امتياز فني درجه ")
        if str(self.selected_option.get()) == "اجازة تعليمية":
            daraja = daraja + 14
            print(daraja, "اجازه تعليميه درجه ")
        if str(self.selected_option.get()) == "شهاده الكفاءه":
            daraja = daraja + 16
            print(daraja, " شهاده الكفاءه درجه")
        return daraja
