# 创建一个文件夹
import os
# os.mkdir("rename")

# 切换到rename地址
# os.chdir("rename")
# 查看当前目录
# ret = os.getcwd()
# print(ret)

# 创建文档
# for i in range(1,11):
#     f = open("%d renametest.txt" % i, "w")
#     f.close()


# 批量修改
# 切换目录
os.chdir("rename")

# 读取rename中的文件列表
my_list = os.listdir()
#遍历my_list
for list_name in my_list:
    new_name = list_name.replace(".txt", "[重命名].txt")
    # print(new_name)
    os.rename(list_name, new_name)


