num=[int(n) for n in input().split()]
n=num[0]
q=num[1]
a=[int(n) for n in input().split()]
shu=[]
for i in range(n):
    shu.append(0)
for i in range(q):
    row=[int(n) for n in input().split()]
    for j in range(row[0]-1,row[1]):
        shu[j]+=1
a.sort()
shu.sort()
res=0
for i in range(n):
    res+=a[i]*shu[i]
print(res)