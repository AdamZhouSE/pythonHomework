a=input().split()
b=input().split()
c=input().split()
for d in range(2):
    a[d]=int(a[d])
for e in range(a[0]):
    b[e]=int(b[e])
for f in range(a[1]):
    c[f]=int(c[f])
res=[]
for i in range(a[1]):
    tem=0
    for j in range(a[0]):
        if b[j]<=c[i]:
            tem+=1
    res.append(tem)
print(' '.join(str(k) for k in res))