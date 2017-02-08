from tkinter import *

window = Tk()
photo = PhotoImage(file="a1.gif")
w = Label(window, image=photo)
w.photo = photo
w.pack()
window.mainloop()
