from tkinter import *

tk = Tk()
Ben_IQ = 100
canvas = Canvas(tk, width=100, height=100, bg='yellow')
canvas.pack()
canvas.create_text(50, 50, text=Ben_IQ, font=('Arial', 50))


def A():
    global Ben_IQ
    Ben_IQ = Ben_IQ + 1
    canvas.delete('all')
    canvas.create_text(50, 50, text=Ben_IQ, font=('Arial', 50))


def B():
    global Ben_IQ
    if Ben_IQ > 100:
        Ben_IQ = Ben_IQ - 1
        canvas.delete('all')
        canvas.create_text(50, 50, text=Ben_IQ, font=('Arial', 50))
    else:
        pass


bt = Button(tk, text='IQ+1', command=A)
bt.pack()
bt2 = Button(tk, text='IQ-1', command=B)
bt2.pack()
tk.mainloop()
