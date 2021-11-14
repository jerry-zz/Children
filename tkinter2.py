y = eval(input('y:'))
x = 100000000000000
for a in range(1, y):
    x = x * a ** 10
print(x)