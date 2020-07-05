rest = eval(input())
veg = int(input())
maxv = int(input())
maxd = int(input())
if veg==1:
    tem = []
    for i in range(0,len(rest)):
        if rest[i][2]==1:
            tem.append(rest[i])
else:
    tem = rest[:]
tem.sort(key = lambda x : x[1])
tem.reverse()
res = []
for i in range(0,len(tem)):
    res.append(tem[i][0])
print(res)