# 新建文件，输入内容
old_f = open("word.txt", "w")
old_f.write("helloworld!!")
old_f.close()

# 备份old_f---伪代码
# 1.打开old_f文件
# 2.读取文件
# 3.新建new—f文件
# 4.将读取的文件放入新文件中


# 1.打开old_f文件
old_f = open("word.txt", "r")
# 2.读取文件
result = old_f.read()
# 3.新建new—f文件
new_f = open("word2.txt", "w")
# 4.将读取的文件放入新文件中
new_f.write(result)