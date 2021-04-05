import os
from tkinter import *

w = 0
h = 100
True_article = ''
file_name = []
cat_name = []
file_list = []
article_name = []
map1 = {}
file_dir = r"C:\Users\jerry\Documents\GitHub\Project\XiaoMingLibrary\Libraries"
for root, dirs, files in os.walk(file_dir):
    file_name = files
    for i in range(0, len(file_name)):
        file_list.append(file_name[i].split("_"))
    for a in range(0, len(file_list)):
        cat_name.append(file_list[a][0])
        article_name.append(file_list[a][1])
        article_name[a] = article_name[a].replace(".txt", "")
        map1['%s' % article_name[a]] = '%s' % cat_name[a]
        cat_name = list(set(cat_name))


def read():
    tk_book = Tk()
    file = open(
        ("C:\\Users\\jerry\\Documents\\GitHub\\Project\\XiaoMingLibrary\\Libraries\\%s" % True_article),
        encoding='utf8').read()
    canvas_book = Canvas(tk_book, width=500, height=500)
    canvas_book.pack()
    canvas.create_text(320, 50, text=('%s' % True_article), font=('Arial', 50))
    canvas.create_text(320, 170, text=file, font=('Arial', 10))


def all_book():
    global True_article
    tk.title('全部图书')
    canvas.delete('all')
    for all_book_book in range(0, len(article_name)):
        bt = Button(tk, text=('%s' % article_name[all_book_book]), command=read())
        bt.pack()
        True_article=article_name[all_book_book]


def start():
    def all_book1():
        bt_all_book.place(x=1000, y=1000)
        all_book()

    tk.title('主页')
    canvas.create_text(250, 100, text='欢迎来到小明图书馆!', font=('Arial', 40), fill='yellow')
    bt_all_book = Button(tk, width=20, height=5, text='所有图书', command=all_book1)
    bt_all_book.pack()
    bt_all_book.place(x=50, y=300)


tk = Tk()
tk.resizable(0, 0)
canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()
bt_quit = Button(tk, text='退出', fg='red', command=tk.quit)
bt_quit.pack()
bt_quit.place(x=450, y=470)
bt_quit = Button(tk, text='主页', command=start)
bt_quit.pack()
bt_quit.place(x=400, y=470)
start()
tk.mainloop()
