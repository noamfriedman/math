from tkinter import *

window = Tk()

window.title("This is a window")
lbl = Label(window, text="Hello", font=("Impact", 70))
lbl.grid(column=0, row=0)

window.mainloop()

