def fun1():
    # 在函数内部定义的变量，叫做局部变量
    # 局部变量的作用域在函数内部，函数外部无法使用
    num = 10
    print(num)
fun1()

def fun2():
    # 不同的函数，相同的局部变量名是不冲突的
    num = 10
    print(num)
fun2()