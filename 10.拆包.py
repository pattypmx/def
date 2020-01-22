#  定义一个列表
my_list = [1, 3.14, "hello", True]
print(my_list[1])   #通过下标索引查找元素，但是可读性不强

#拆包，变量和数值要一一对应
my_int, pi, my_str, my_bool = my_list
print(my_str)
#  my_int, pi, my_str, my_bool = [1, 3.14, "hello", True]

#   定义一个元组
my_tuple = (1, 3.14, "hello", True)
my_int, pi, my_str, my_bool = my_tuple
print(my_bool)

#   定义一个元组
my_dict = {"姓名":"小明", "年龄":12}
my_name, my_age = my_dict
print(my_name, my_age)  # 只输出key值

def fun(name, age):
    new_name = "姓名:%s" % name
    new_age = "年龄:%d" % age
    return new_name,new_age
# ret = fun("小明", 12)
newest_name, newest_age = fun("小明", 12)
print(newest_name, newest_age)