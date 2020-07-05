e=input().split()
N=int(e[0])
G=int(e[1])
a=[G]*100
b=[]
s=[]
res=0
for i in range(0,N):
    b=b+[input().split()]
for i in range(0,N):
    for j in range(0,len(b[i])):
        b[i][j]=int(b[i][j])
for i in range(0, N):
    for j in range(0, N - 1):
        if b[j][0] > b[j + 1][0]:
            b[j], b[j + 1] = b[j + 1], b[j]
for i in range(0,len(b)):
    t=[]+s
    s=[]
    x=b[i][1]-1
    n=b[i][2]
    a[x]=a[x]+n
    m=max(a)
    for j in range(0,len(a)):
        if a[j]==m:
            s=s+[a[j]]
    if s!=t:
        res=res+1
print(res,end='')


