# 有一字符串，包含n个字符。写一函数，将此字符串中从第m个字符开始的全部字符复制成为另一个字符串。
length = int(input())
string = input()
m = int(input())
res = ""
for i in range(m-1, length):
    res = res + string[i]
print(res)
