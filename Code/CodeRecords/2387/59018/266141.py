def sorts(a,OP,L,R):    
    c=[]    
    d=[]
    for j in range(len(a)):
        if L<=a[j]<=R:
            c.append(j)
            d.append(a[j])
    if OP==0:
        d.sort()
    else:
        d.sort(reverse=True)
    for j in c:
        a[j]=d[0]
        del d[0]
    return a

n1,m1=input().split(' ')
n=int(n1)
m=int(m1)
info=input().split(' ')
a=[int(y) for y in info]
for i in range(m):
    OP1,L1,R1=input().split(' ')
    OP=int(OP1)
    L=int(L1)
    R=int(R1)
    c=[]    
    d=[]
    for j in range(len(a)):
        if L<=a[j]<=R:
            c.append(j)
            d.append(a[j])
    if OP==0:
        d.sort()
    else:
        d.sort(reverse=True)
    for j in c:
        a[j]=d[0]
        del d[0]
q=int(input())    
print(a[q])        
    
      