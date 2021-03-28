from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=500, height=500, bg='black')
canvas.pack()
canvas.create_text(250, 100, text='欢迎来到小明图书馆!', font=('Arial', 40), fill='yellow')


def all_book():
    tk_all_book = Tk()

    def story():
        tk_story = Tk()

        def tortoise_hare_race():
            tk_tortoise_hare_race = Tk()
            canvas = Canvas(tk_tortoise_hare_race, width=590, height=300)
            canvas.pack()
            canvas.create_text(295, 50, text='龟兔赛跑', font=('Arial', 40))
            canvas.create_text(300, 170, text='''    在一个风和日丽的上午，小兔和小乌龟去山上看鲜花，小兔一蹦一跳地跑在前面，小乌龟慢吞
吞地在后面爬，小兔觉得小乌龟爬得太慢了，就傲慢地对小乌龟说：“嗨，小乌龟，我们来一
场比赛吧，看看谁先到达山顶。”“哼，比就比。”小乌龟说。'
    于是，它们请来斑马当裁判。枪声一响，小兔就像离弦的剑一样跑了出去，一下就不见了踪
影，小兔跑啊跑，回头一看，小乌龟才刚刚爬过起跑线，心想：“小乌龟爬得太慢，一定追不'
上我，我也有点累了，休息一下睡一会儿也没关系。”
    小兔躺在草地上呼呼大睡，过了一会儿，小乌龟追了上来，它看见小兔在睡觉，便不顾劳累，
鼓足劲，努力地向终点爬去。
    小兔一觉醒来，还不见小乌龟的踪影，便不紧不慢地向山顶跑去，到了终点，小兔看见大家都
在向小乌龟表示祝贺，惭愧地低下了头，灰溜溜地走了，心想：“我以后再也不能骄傲了。”''', font=('Arial', 10))

        def Waiting_for_another_hare():
            tk_Waiting_for_another_hare = Tk()
            canvas = Canvas(tk_Waiting_for_another_hare, width=640, height=250)
            canvas.pack()
            canvas.create_text(285, 50, text='守株待兔', font=('Arial', 50))
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

        canvas = Canvas(tk_story, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='童话类', font=('Arial', 70), fill='white')
        bt_quit_story = Button(tk_story, width=10, height=1, text='退出', fg='red', command=tk_story.quit)
        bt_quit_story.pack()
        bt_quit_story.place(x=400, y=450)
        bt_ = Button(tk_story, width=10, height=2, text='龟兔赛跑', command=tortoise_hare_race)
        bt_.pack()
        bt_.place(x=0, y=100)
        bt_ = Button(tk_story, width=10, height=2, text='守株待兔', command=Waiting_for_another_hare)
        bt_.pack()
        bt_.place(x=0, y=150)
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
        canvas = Canvas(tk_prose, width=500, height=500, bg='black')
        canvas.pack()
        canvas.create_text(250, 50, text='散文类', font=('Arial', 70), fill='white')
        bt_quit_prose = Button(tk_prose, width=10, height=1, text='退出', fg='red', command=tk_prose.quit)
        bt_quit_prose.pack()
        bt_quit_prose.place(x=400, y=450)

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
