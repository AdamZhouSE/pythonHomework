# 字符串分类统计？
def rev(string):
    string = string[::-1]
    return string


s = input()
print(rev(s), end='')
# print末尾默认换行，这里使得其末尾为null