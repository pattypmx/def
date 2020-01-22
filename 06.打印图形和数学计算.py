# 自定义打印横线行数
def line():
    print("-"*5)

def lines(num):
    for x in range(num):
        line()
lines(5)


# 求三个函数的和
def sum(a, b, c):
    return a + b + c
sum_one = sum(1, 2, 3)
print(sum_one)

# 求三个函数的平均值
def avg(num1, num2, num3):
    ret = sum(num1, num2, num3)
    return ret / 3
result = avg(1, 2, 3)
print(result)