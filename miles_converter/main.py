from tkinter import *


def calculate():
    miles_input = float(my_input.get())
    result = round(miles_input * 1.609, 3)
    label3.config(text=result)


window = Tk()
window.minsize(50, 30)
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
my_input = Entry(width=5)
my_input.grid(column=1, row=0)

label1 = Label(text="Miles", font=("Arial", 14, "bold"))
label1.grid(column=2, row=0)
label1.config(padx=5, pady=5)

label2 = Label(text="is equal to ", font=("Arial", 14, "bold"))
label2.grid(column=0, row=1)
label2.config(padx=5, pady=5)

label3 = Label(text=0, font=("Arial", 14, "bold"))
label3.grid(column=1, row=1)
label3.config(padx=5, pady=5)

label4 = Label(text="KM", font=("Arial", 14, "bold"))
label4.grid(column=2, row=1)
label4.config(padx=5, pady=5)

my_button = Button(text="Calculate", command=calculate)
my_button.grid(column=1, row=2)
my_button.config(padx=5, pady=5)



window.mainloop()
