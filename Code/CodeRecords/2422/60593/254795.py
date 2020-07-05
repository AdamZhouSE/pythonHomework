import random
def rS(a,l,r):
    global cop
    lop[cop]=l
    rop[cop]=r
    cop+=1
    ap=l
    for i in range(l+1,r+1,2):
        tmp[i]=a[ap]
        ap+=1
    for i in range(l,r+1,2):
        tmp[i]=a[ap]
        ap+=1
    for i in range(l,r+1):
        a[i]=tmp[i]
def sol(a):
    for i in range(n,0,-1):
        for j in range(1,i):
            if(a[j]==i):
                rad=min(j,i-j)
                rS(a,j-rad+1,j+rad)
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
b=[0]*(n+1)
for i in range(1,n+1):
    b[i]=i
random.shuffle(b)
rb=[0]*3333
ra=[0]*3333
tmp=[0]*3333
for i in range(1,n+1):
    rb[b[i]]=i
for i in range(1,n+1):
    a[i]=rb[a[i]]
for i in range(1,n+1):
    ra[a[i]]=i
lop=[0]*15555
rop=[0]*15555
cop=0
sol(rb)
sol(ra)
print(cop)
for i in range(cop-1,-1,-1):
    print(lop[i],rop[i])
