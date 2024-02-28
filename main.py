from tkinter import *


def calculate_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    Kilometer_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)

is_equal_to = Label(text="is equal to", font=("Arial", 20))
is_equal_to.grid(column=1, row=3)

Kilometer_label = Label(text="0")
Kilometer_label.grid(column=2, row=3)

miles_input = Entry(width=15)
print(miles_input.get())
miles_input.grid(column=2, row=2)

miles = Label(text='Miles', font=('Arial', 20))
miles.grid(column=3, row=2)

km = Label(text="KM", font=('Arial', 20))
km.grid(column=3, row=3)

calculate = Button(text="Calculate", font="Arial", command=calculate_km)
calculate.grid(column=2, row=4)

window.mainloop()
