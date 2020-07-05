num=[int(n) for n in input().split()]
n=num[0]
m=num[1]
d=num[2]
shu=[]
res=99999
for i in range(n):
    row=[int(n) for n in input().split()]
    for j in range(m):
        shu.append(row[j])
for i in range(len(shu)):
    cunzai =True
    for j in range(len(shu)):
        if abs(shu[j]-shu[i])%d!=0:
            cunzai=False
            break
    if cunzai:
        need=0
        for j in range(len(shu)):
            need+=int(abs(shu[j]-shu[i])/d)
        res=min(res,need)
if res==99999:
    res=-1
print(res)