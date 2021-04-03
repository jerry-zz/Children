import time
from tkinter import *


def go():
    a = canvas.create_text(250, 250, text='')
    canvas.delete(a)
    time.sleep(1)
    t = time.localtime()
    year = t[0]
    month = t[1]
    month_day = t[2]
    hour = t[3]
    minute = t[4]
    second = t[5]
    week_day = t[6] + 1
    a = canvas.create_text(250, 250, text=second)
    go()


tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
bt = Button(tk, text='开始', command=go)
bt.pack()
tk.mainloop()
