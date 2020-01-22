# 定义函数，根据分数返回优良中差
def score(num):
    """
    根据分数返回优良中差
    :param num:分数
    :return:返回的数
    """
    if num < 0:
        print("传入分数有误！！！")
        return # 传入有误，函数提前结束，提高性能，不然python会一直执行下去
    elif num >= 90:
        return "优"
    elif num >= 75:
        return "良"
    elif num >= 60:
        return "中"
    elif num > 0:
        return "差"
ret = score(88)
print(ret)

def fun():
    print("haha")
    # 只要函数执行了return，提前结束函数的执行，return后面的将不会执行
    return 3.14
    print("heihei")
    return 3333
ret2 = fun()
print(ret2)
help(score)