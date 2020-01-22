def fun(a, b):  # ab为行参
    ret = a + b
    print(ret)
fun(10, 20) # 10，20为实参


def fun(name):  # name为行参
    print("你好%s" % name)
fun("xiaoming")    # xiaoming为实参