def fun(name, no, age):
    print("姓名：%s" % name)
    print("编号：%s" % no)
    print("年龄：%d" % age)
    print("="*10)

fun("小红", "001", 20)
fun("小明", "002", 20)
fun("小哈", "003", 20)

# 定义一个缺省参数的函数
# 缺省参数：给函数设定一个默认值
def fun(name, no, age=20):
    print("姓名：%s" % name)
    print("编号：%s" % no)
    print("年龄：%d" % age)
    print("="*10)
# 在调用函数时，如果有默认值，可根据业务需求不传递
# 如果小红是30岁，其他都是20岁
fun("小红", "001", 30)
fun("小明", "002")
fun("小哈", "003")
