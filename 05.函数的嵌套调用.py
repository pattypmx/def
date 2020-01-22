def fun1():
    print("2"*5)
    print("3"*5)
# fun1()

def fun2():
    print("1"*5)
    fun1()
    print("4"*5)
fun2()
