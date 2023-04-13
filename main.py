from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


# pyinstaller --icon=pomodoro.ico --add-data "tomato.png;." --noconsole pomodoro.py

window = Tk()
window.title("My GUI")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)

#label
my_label = Label(text="my label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#button
my_button = Button(text="click me", command=button_clicked)
my_button.grid(column=1, row=1)

#new_button
my_new_button = Button(text="click me", command=button_clicked)
my_new_button.grid(column=2, row=0)


#entry
input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()