import time
from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
tk.mainloop()
while 1:
    t = time.localtime()
    year = t[0]
    month = t[1]
    month_day = t[2]
    hour = t[3]
    minute = t[4]
    second = t[5]
    week_day = t[6] + 1
    h_m_s = hour, minute, second
    print(h_m_s)
