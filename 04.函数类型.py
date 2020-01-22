# 无参数，无返回值
def fun():
    print("nihaoya")
fun()

# 无参数，有返回值
def fun2():
    return 11
print(fun2())

# 有参数，无返回值
def fun3(name):
    print("名字:", name)
fun3("xioaming")


# 多个姓名轮流娴熟
# 先定义一个列表
def fun4(name):
    print("名字:", name)

name_list = {"小明", "小红", "哈哈", "妮妮"}
for new_name in name_list:
    fun4(new_name)

# 有参数，有返回值
def fun5(a, b):
    ret = a + b
    return ret
num = fun5(10, 10)
print(num)

