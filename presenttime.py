import turtle, time
import random


def drawLine(draw):
    colors = ['red', 'black', 'green', 'blue', 'yellow', 'purple', 'mauve', 'scarlet']
    a = random.randint(1, 8)
    turtle.pencolor(colors[8 % a])
    turtle.penup()
    turtle.fd(5)
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(35)
    turtle.penup()
    turtle.fd(5)
    turtle.right(90)


def drawDigts(n):
    drawLine(True) if n in ['2', '3', '4', '5', '6', '8', '9'] else drawLine(False)
    drawLine(True) if n in ['0', '1', '3', '4', '5', '6', '7', '8', '9'] else drawLine(False)
    drawLine(True) if n in ['0', '2', '3', '5', '6', '8', '9'] else drawLine(False)
    drawLine(True) if n in ['0', '2', '6', '8'] else drawLine(False)
    turtle.left(90)
    drawLine(True) if n in ['0', '4', '5', '6', '8', '9'] else drawLine(False)
    drawLine(True) if n in ['0', '2', '3', '5', '6', '7', '8', '9'] else drawLine(False)
    drawLine(True) if n in ['0', '1', '2', '3', '4', '7', '8', '9'] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(10)


def drawDate(date):
    for i in range(0, len(date)):
        drawDigts(date[i])
        if date[i] == '-':
            turtle.penup()
            turtle.right(90)
            turtle.fd(30)
            turtle.left(90)
            turtle.pendown()
            turtle.write('年', align='center', font=('Arial', 52, 'normal',))
            turtle.penup()
            turtle.left(90)
            turtle.fd(30)
            turtle.right(90)
            turtle.fd(60)
        elif date[i] == '+':
            turtle.penup()
            turtle.right(90)
            turtle.fd(30)
            turtle.left(90)
            turtle.pendown()
            turtle.write('月', font=('Arial', 52, 'normal'))
            turtle.penup()
            turtle.left(90)
            turtle.fd(30)
            turtle.right(90)
            turtle.fd(60)
        elif date[i] == '=':
            turtle.penup()
            turtle.right(90)
            turtle.fd(30)
            turtle.left(90)
            turtle.pendown()
            turtle.write('日', font=('Arial', 52, 'normal'))
            turtle.penup()
            turtle.left(90)
            turtle.fd(30)
            turtle.right(90)
            turtle.fd(60)


turtle.setup(1000, 600, 500, 500)
turtle.hideturtle()
turtle.penup()
turtle.bk(380)
date = time.strftime('%Y-%m+%d=', time.gmtime())
turtle.pendown()
drawDate(date)
turtle.exitonclick()
