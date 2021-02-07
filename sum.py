#先定义一个变量保存和
#python是一个弱类型的语言，变量是没数据类型的
sum = 0
#使用循环解决累加求和
num = 1
while num < 101:
    sum += num
    num = num + 1
print('1到100的和是')
print(sum)
