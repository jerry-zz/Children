from tkinter import *

V = 10
tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
ball_id = canvas.create_oval(10, 10, 25, 25, fill='red')
canvas.pack()
canvas.move(ball_id, 250, 250)


def up():
    canvas.move(ball_id, 0, -V)


def down():
    canvas.move(ball_id, 0, V)


def left():
    canvas.move(ball_id, -V, 0)


def right():
    canvas.move(ball_id, V, 0)


bt_up = Button(tk, width=5, height=5, text='上', command=up)
bt_up.pack()
bt_down = Button(tk, width=5, height=5, text='下', command=down)
bt_down.pack()
bt_left = Button(tk, width=5, height=5, text='左', command=left)
bt_left.pack()
bt_right = Button(tk, width=5, height=5, text='右', command=right)
bt_right.pack()
bt_up.place(x=250, y=10)
bt_down.place(x=250, y=110)
bt_right.place(x=300, y=60)
bt_left.place(x=200,y=60)
tk.mainloop()
