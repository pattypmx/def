# 有些时候，需要对文件进行重命名、删除等一些操作，python的os模块中都有这么功能
# 重命名
import os
# os.rename("wenzi1.txt", "wenzi11.txt")

# 创建文件
# p = open("haha.txt", "w")

# 删除文件
# os.remove("word3.txt")

# ----------------------------

#创建文件夹
# os.mkdir("helloword")
# os.mkdir("helloword.txt")

# 删除文件夹
# os.rmdir("helloword.txt")

# ----------------------------

# 获取当前目录    获取的是绝对路径，可以看到盘符
# ret = os.getcwd()
# print(ret)

# 改变默认目录
# ../ 上一级目录；./或者../都是相对路径
# os.chdir("../")
# ret1 = os.getcwd()
# print(ret1)

# 获取目录列表
ret2 = os.listdir()
print(ret2)

