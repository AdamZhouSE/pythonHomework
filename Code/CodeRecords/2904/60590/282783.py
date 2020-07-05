num = int(input())
flag = False
s1 = ""
if num == 0:
    s1 = "0"
else:
    if num < 0:
        num = -num
        flag = True
    s = str(num)
    s1 = s[::-1]
    #print(s1)
    index = 0
    while s1[index] == '0':
        index = index +1
    #print("index: ", end="")
    #print(index)
    s1 = s1[index : s1.__len__()]
    if flag:
        s1 = "-" + s1
print(s1)