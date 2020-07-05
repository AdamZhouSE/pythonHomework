n,m=input().split(' ')
info1=input().split(' ')
a=[int(y) for y in info1]
info2=input().split(' ')
b=[int(x) for x in info2]
c=[]
for i in range(len(b)):
    count=0
    for j in range(len(a)):
        if a[j]<=b[i]:
            count=count+1
    c.append(count)
d=[str(z) for z in c]
print(' '.join(d))
            
            
            
                   