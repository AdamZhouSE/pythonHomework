def chaban(num,weizhi,k,oc,zc):
    if weizhi == len(num) or num == []:
        return
    if k==0:
        zc.append(num)
        oc.append(zc)
        return
    chaban(num,weizhi+1,k,oc,zc.copy())
    zc1=num.copy()
    zc2=[]
    for i in range(weizhi+1):
        zc2.append(num[i])
    zc3=zc.copy()
    zc3.append(zc2)
    for i in range(weizhi+1):
        zc1.remove(num[i])
    chaban(zc1,0,k-1,oc,zc3)
num=[int(n) for n in input().split()]
n=num[0]
k=num[1]
num=[int(n) for n in input().split()]
oc=[]
chaban(num,0,k-1,oc,[])
oc2=[]
for i in oc:
    zs=0
    for j in i:
        zs+=j[len(j)-1]-j[0]
    oc2.append(zs)
oc2.sort()
print(oc2[0])