# 自定义排序---最外层肯定是列表
my_list = [ {"name": "zhangsan", "age": 18},
            {"name": "lisi", "age": 19},
            {"name": "wangwu", "age": 17}]
# 按年龄排序
my_list.sort(key=lambda new_list : new_list["age"])
print(my_list)

# 按照姓名排序,是基于ASCII码排的
my_list.sort(key=lambda new_list2 : new_list2["name"])
print(my_list)

my_list2 = [[1, 2, 3], [4, 8, 2], [5, 6, 0]]
# 按照第2个数排序
my_list2.sort(key=lambda new_list3 : new_list3[1])
print(my_list2)
# 降序
my_list2.sort(key=lambda new_list4 : new_list4[1], reverse=True)
print(my_list2)
