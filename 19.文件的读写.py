# 写数据
# 如果文件不存在那么创建，如果存在那么就先清空，然后写入数据
# f = open("wenzi2.txt", "w")
# f.write("hello world")
# f.close()

# 读数据
f = open("wenzi2.txt", "r")
# # 读取3位
ret = f.read(3)
print(ret)
ret = f.read(3)
print(ret)
# # 从上次读取的位置继续读取剩下的所有的数据
ret = f.read()
print(ret)
f.close()

# a 在现有文字后面追加文字
f = open("wenzi2.txt", "a")
ret1 = f.write("\nhahaha")
f.close()

# 读数据，以只读模式读取，且以列表形式展现
f = open("wenzi2.txt", "r")
ret2 = f.readlines()
print(ret2)
f.close()
