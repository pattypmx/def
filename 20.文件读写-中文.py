# 默认中文为gbk，win系统需要添加utf-8，mac和linux不需要
# f = open("zhongwen.txt", "w", encoding= utf-8)
f = open("zhongwen.txt", "w")
ret = f.write("哈哈，你好")
f.close()

# f = open("zhongwen.txt", "r", encoding= utf-8)
f = open("zhongwen.txt", "r")
ret1 = f.read()
print(ret1)
f.close()