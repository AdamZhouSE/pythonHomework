total = int(input())
res = []
resu = []
for i in range(0,total):
    ls = input()
    res.append(ls)
for i in range(0,total):
    tem = []
    mark = ''
    for j in range(0,len(res[i])):
        if res[i][j] == mark:
            continue
        else:
            mark = res[i][j]
            tem.append(res[i][j])
    str = ''.join(tem)
    resu.append(str)
for i in range(0,total):
    print(resu[i])
    