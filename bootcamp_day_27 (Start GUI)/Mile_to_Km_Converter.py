from tkinter import *


def convert_mile_to_km():
    km = float(user_input.get()) * 1.609344
    result_lab.config(text=km)


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# Labels
Miles_lab = Label(text="Miles")
Miles_lab.config(padx=20, pady=5)
Miles_lab.grid(column=2, row=0)

Km_lab = Label(text="Km")
Km_lab.config(padx=20, pady=5)
Km_lab.grid(column=2, row=1)

text_lab = Label(text="is equal to")
text_lab.config(padx=20, pady=5)
text_lab.grid(column=0, row=1)

result_lab = Label(text=0)
result_lab.grid(column=1, row=1)

# Entry
user_input = Entry()
user_input.insert(END, string=0)
user_input.grid(column=1, row=0)

# Button
Calc_but = Button(text="Calculate", cursor="hand1", command=convert_mile_to_km)
Calc_but.grid(column=1, row=2)

window.mainloop()
# EoF (End of File)
