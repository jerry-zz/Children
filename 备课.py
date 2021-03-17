from tkinter import *

tk = Tk()
level = 0
tk.title('Game')


def b():
    return level == level + 1


def c():
    return level == level - 1


def a():
    print(level)


bt1 = Button(tk, text='+1', command=b)
bt1.pack()
bt2 = Button(tk, text='-1', command=c)
bt2.pack()
bt3 = Button(tk, text='打印', command=a)
bt3.pack()
tk.mainloop()
