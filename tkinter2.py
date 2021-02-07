from tkinter import *


def hello():
    print('hello!')


tk = Tk()
btn = Button(tk, text='click me', command=hello)
btn.pack()


tk.mainloop()
