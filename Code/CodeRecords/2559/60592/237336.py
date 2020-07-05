total = int(input())
str = []
res = []
for i in range(0,total):
    ls = input()
    str.append(ls)
for i in range(0,total):
    tem = []
    for j in range(0,len(str[i])):
        if str[i][j] in tem:
            res.append(0)
            break
        else:
            tem.append(str[i][j])
        if j ==len(str[i])-1:
            res.append(1)
for i in range(0,total):
    print(res[i])