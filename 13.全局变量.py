# 1.全局变量:定义在函数外部，既能在一个函数中使用，也能在其他的函数中使用
num = 10

def fun1():
    print("fun1:", num)
fun1()

def fun2():
    print("fun2:", num)
fun2()

# 2.全局+局部变量
num1 = 22
def fun3():
    num1 = 33
    print("fun3:", num1)
fun3()
print("fun3全局:", num1)

# 3.局部变量强制转换全局变量
num3 = 44
def fun4():
    global num3
    num3 = 55
    print("fun4:", num3)
fun4()
print("外部：", num3)

