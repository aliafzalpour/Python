from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=40, pady=40)

is_equal = Label(text="is equal to", font=("Arial", 12))
is_equal.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Arial", 12))
km_label.grid(column=2, row=1)

miles_to_km = Label(text="0", font=("Arial", 12))
miles_to_km.grid(column=1, row=1)

def miles_to_kilometers():
    miles_input = user_input.get()
    miles_to_km_input = float(miles_input)
    if miles_input.isdigit() and miles_to_km_input > 0 and not None:
        km_output = round((miles_to_km_input * 1.60934), 2)
        miles_to_km.configure(text=f"{km_output}")

button = Button(text="Calculate", command=miles_to_kilometers)
button.grid(column=1, row=2)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

window.mainloop()