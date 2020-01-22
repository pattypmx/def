# 无参数无返回值
def fun1():
    print("nihao")
fun1()
# 匿名
fun11 = lambda : print("nihao")
fun11()
# 等价于
(lambda : print("nihao"))()

#无参数有返回值
def fun2():
    return 3.14
print(fun2())

fun22 = lambda : 3.14
print(fun22())

# 有参数无返回值
def fun3(name):
    print("nihao:",name)
fun3("小明")

fun33 = lambda name :print("nihao:",name)
fun33("小明")

#有参数有返回值
def fun4(a, b):
    num = a + b
    return num
sum = fun4(1, 2)
print(sum)

fun44 = lambda a, b : a + b
print(fun44(1, 2))
