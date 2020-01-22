# 定义函数
f = lambda x, y : x + y # opt = lambda x, y : x + y
def fun(a, b, opt):
    print("a=", a)
    print("b=", b)
    # result = opt(a, b)
    # print("result=", result)

    print("result=", opt(a, b))

fun(1, 2, f)
# 就是函数嵌套