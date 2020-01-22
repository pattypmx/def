# 列表推导式，指的是轻量级循环创建列表
# 1.将1-10存入列表
my_list = []
for i in range(1, 11):
    my_list.append(i)
print(my_list)
# 列表推导式
my_list1 = [i for i in range(1, 11)]
print(my_list1)

my_list11 = [i for i in range(1,11,2)]
print(my_list11)
#---------------------------

# 2.打印5个"哈哈"
my_list2 = ["哈哈" for i in range(5)]
print(my_list2)
#---------------------------

# 3.打印1-20的偶数
my_list3 = []
for i in range(1, 21):
    if i % 2 == 0:
        my_list3.append(i)
print(my_list3)
# 列表推导式
my_list33 = [i for i in range(1, 21) if i % 2 == 0]
print(my_list33)

