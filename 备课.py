from tkinter import *

tk = Tk()
tk.resizable(0, 0)
tk.title('主页')
canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()
canvas.create_text(250, 100, text='欢迎来到小明图书馆!', font=('Arial', 40), fill='yellow')


def all_book():
    tk_all_book = Tk()
    tk_all_book.resizable(0, 0)

    def story():
        tk_story = Tk()
        tk_story.resizable(0, 0)

        def tortoise_hare_race():

            tk_tortoise_hare_race = Tk()
            tk_tortoise_hare_race.resizable(0, 0)
            tk_tortoise_hare_race.title('龟兔赛跑')
            canvas = Canvas(tk_tortoise_hare_race, width=700, height=300)
            canvas.pack()
            canvas.create_text(350, 50, text='龟兔赛跑', font=('Arial', 50))
            canvas.create_text(350, 170, text=, font=('Arial', 11))

        def Waiting_for_another_hare():
            tk_Waiting_for_another_hare = Tk()
            tk_Waiting_for_another_hare.resizable(0, 0)
            tk_Waiting_for_another_hare.title('守株待兔')
            canvas = Canvas(tk_Waiting_for_another_hare, width=640, height=250)
            canvas.pack()
            canvas.create_text(320, 50, text='守株待兔', font=('Arial', 50))
            canvas.create_text(320, 170, text='''    春秋时代有位宋国的农夫，他每天早上很早就到田里工作，一直到太阳下山才收拾农具准备回家。

    有一天，农夫正在田里辛苦的工作，突然却远远跑来一只兔子。这只兔子跑得又急又快，一个不小心
，兔子撞上稻田旁边的大树，这一撞，撞断了兔子的颈部，兔子当场倒地死亡。
    一旁的农夫看到之后，急忙跑上前将死了的兔子一手抓起，然后很开心的收拾农具准备回家把这只兔
子煮来吃。农夫心想，天底下既然有这么好的事，自己又何必每天辛苦的耕田？
    从此以后，他整天守在大树旁，希望能再等到不小心撞死的兔子。可是许多天过去了，他都没等到撞
死在大树下的兔子，反而因为他不处理农田的事，因此田里长满了杂草，一天比一天更荒芜。 ''', font=('Arial', 10))

        def B():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        def C():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        def D():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        tk_story.title('童话类')
        canvas = Canvas(tk_story, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='童话类', font=('Arial', 70), fill='white')
        bt_quit_story = Button(tk_story, width=10, height=1, text='退出', fg='red', command=tk_story.quit)
        bt_quit_story.pack()
        bt_quit_story.place(x=400, y=450)
        bt_tortoise_hare_race = Button(tk_story, width=10, height=2, text='龟兔赛跑', command=tortoise_hare_race)
        bt_tortoise_hare_race.pack()
        bt_tortoise_hare_race.place(x=0, y=100)
        bt_Waiting_for_another_hare = Button(tk_story, width=10, height=2, text='守株待兔',
                                             command=Waiting_for_another_hare)
        bt_Waiting_for_another_hare.pack()
        bt_Waiting_for_another_hare.place(x=0, y=150)
        bt_ = Button(tk_story, width=10, height=2, text='', command=B)
        bt_.pack()
        bt_.place(x=0, y=200)
        bt_ = Button(tk_story, width=10, height=2, text='', command=C)
        bt_.pack()
        bt_.place(x=0, y=250)
        bt_ = Button(tk_story, width=10, height=2, text='', command=D)
        bt_.pack()
        bt_.place(x=0, y=300)

    def prose():
        tk_prose = Tk()
        tk_prose.resizable(0, 0)

        def fast():
            tk_fast = Tk()
            tk_fast.resizable(0, 0)
            tk_fast.title('匆匆')
            canvas = Canvas(tk_fast, width=740, height=400)
            canvas.pack()
            canvas.create_text(370, 50, text='匆匆', font=('Arial', 50))
            canvas.create_text(370, 250, text='''       燕子去了，有再来的时候；杨柳枯了，有再青的时候；桃花谢了，有再开的时候。但是，聪明的，你
告诉我，我们的日子为什么一去不复返呢？——是有人偷了他们罢：那是谁？又藏在何处呢？是他
们自己逃走了罢：现在又到了哪里呢？
        我不知道他们给了我多少日子；但我的手确乎是渐渐空虚了。在默默里算着，八千多日子已经从
我手中溜去；像针尖上一滴水滴在大海里，我的日子滴在时间的流里，没有声音，也没有影子。
我不禁头涔涔而泪潸潸了。
        去的尽管去了，来的尽管来着；去来的中间，又怎样地匆匆呢？早上我起来的时候，小屋里射进
两三方斜斜的太阳。太阳他有脚啊，轻轻悄悄地挪移了；我也茫茫然跟着旋转。于是——洗手的时
候，日子从水盆里过去；吃饭的时候，日子从饭碗里过去；默默时，便从凝然的双眼前过去。我
觉察他去的匆匆了，伸出手遮挽时，他又从遮挽着的手边过去，天黑时，我躺在床上，他便伶伶
俐俐地从我身上跨过，从我脚边飞去了。等我睁开眼和太阳再见，这算又溜走了一日。我掩着面
叹息。但是新来的日子的影儿又开始在叹息里闪过了。
        在逃去如飞的日子里，在千门万户的世界里的我能做些什么呢？只有徘徊罢了，只有匆匆罢了；
在八千多日的匆匆里，除徘徊外，又剩些什么呢？过去的日子如轻烟，被微风吹散了，如薄雾，
被初阳蒸融了；我留着些什么痕迹呢？我何曾留着像游丝样的痕迹呢？我赤裸裸来到这世界，转
眼间也将赤裸裸的回去罢？但不能平的，为什么偏要白白走这一遭啊？
        你聪明的，告诉我，我们的日子为什么一去不复返呢？''', font=('Arial', 12))

        def C():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        def D():
            tk_ = Tk()
            canvas = Canvas(tk_, width=500, height=500)
            canvas.pack()

        tk_prose.title('散文类')
        canvas = Canvas(tk_prose, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='散文类', font=('Arial', 70), fill='white')
        bt_quit_prose = Button(tk_prose, width=10, height=1, text='退出', fg='red', command=tk_prose.quit)
        bt_quit_prose.pack()
        bt_quit_prose.place(x=400, y=450)
        bt_fast = Button(tk_prose, width=10, height=2, text='匆匆', command=fast)
        bt_fast.pack()
        bt_fast.place(x=0, y=100)
        bt_ = Button(tk_prose, width=10, height=2, text='', command=C)
        bt_.pack()
        bt_.place(x=0, y=150)
        bt_ = Button(tk_prose, width=10, height=2, text='', command=D)
        bt_.pack()
        bt_.place(x=0, y=200)

    tk_all_book.title('全部图书')
    canvas = Canvas(tk_all_book, width=500, height=500, bg='black')
    canvas.pack()
    canvas.create_text(250, 50, text='全部图书', font=('Arial', 70), fill='blue')
    bt_quit_all_book = Button(tk_all_book, width=10, height=1, text='退出', fg='red', command=tk_all_book.quit)
    bt_quit_all_book.pack()
    bt_quit_all_book.place(x=400, y=450)
    bt_story = Button(tk_all_book, width=20, height=5, text='童话类', command=story)
    bt_story.pack()
    bt_story.place(x=0, y=100)
    bt_prose = Button(tk_all_book, width=20, height=5, text='散文类', command=prose)
    bt_prose.pack()
    bt_prose.place(x=0, y=200)


bt_all_book = Button(tk, width=20, height=5, text='所有图书', command=all_book)
bt_all_book.pack()
bt_all_book.place(x=50, y=300)
bt_quit = Button(tk, width=20, height=5, text='退出', fg='red', command=tk.quit)
bt_quit.pack()
bt_quit.place(x=300, y=300)
tk.mainloop()
