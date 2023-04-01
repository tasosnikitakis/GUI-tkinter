from tkinter import *


def button_clicked():
    miles = float(input.get())
    km = 1.609344 * miles
    label2.config(text=km)

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=400, height=300)
window.config(padx=10, pady=10)

#label1
label1 = Label(text="is equal to:", font=("Arial", 16, "bold"))
label1.grid(column=0, row=1)


#label2
label2 = Label(text="0", font=("Arial", 16, "bold"))
label2.grid(column=1, row=1)


#label3
label3 = Label(text="Miles", font=("Arial", 16, "bold"))
label3.grid(column=2, row=0)


#label4
label1 = Label(text="Km", font=("Arial", 16, "bold"))
label1.grid(column=2, row=1)


#entry
input = Entry(width=10)
input.grid(column=1, row=0)


#button
my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(column=1, row=2)



window.mainloop()