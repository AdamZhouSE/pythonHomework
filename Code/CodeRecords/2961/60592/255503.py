ls = input()
tem = []
lsn = ls+ls
for i in range(0,len(ls)):
    tem.append(lsn[i:i+len(ls)])
tem.sort()
res = []
for i in range(0,len(ls)):
    res.append(tem[i][len(ls)-1])
print("".join(res),end='')