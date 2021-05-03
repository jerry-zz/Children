while 1:
    x = eval(input('x:'))
    y = eval(input('y:'))
    if y >= 0:
        print(x ** 2 + 2 * y)
    else:
        print(x ** 2 - 2 * y)
