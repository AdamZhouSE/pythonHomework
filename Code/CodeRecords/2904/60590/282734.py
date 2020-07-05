num = int(input())
flag = False
if num == 0:
    s1 = "0"
else:
    if num < 0:
        num = -num
        flag = True
    s = str(num)
    s1 = s[::-1]
    # print(s1)
    res = ""
    index = 0
    while s1[index] == '0':
        s1 = s1[index + 1: s1.__len__()]
        index = index + 1
    if flag:
        s1 = "-" + s1
print(s1)