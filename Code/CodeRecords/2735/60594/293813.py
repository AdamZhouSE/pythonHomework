num=[int(n) for n in input().split()]
n=num[0]
m=num[1]
num=[int(n) for n in input().split()]
for i in range(m):
    row=[int(n) for n in input().split()]
    l=row[0]
    r=row[1]
    k=row[2]
    zc=[]
    for index in range(l-1,r):
       zc.append(row[index])
    zc.sort()
    print(zc[k-1])