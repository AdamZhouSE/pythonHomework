N=int(input())
a=[0 for i in range(99999)]
b=[]
for i in range(N):
    start,end=map(int,input().split())
    c=[0 for k in range(99999)]
    for j in range(start-1,end-1):
        a[j]+=1
        c[j]+=1
    b.append(c)
l=0
d=[]
for i in range(N):
    e=[]
    for j in range(len(a)):
        e.append(a[j]-b[i][j])
    d.append(e)
f=[]
for i in range(N):
    num=0
    for j in range(1,N):
        num+=d[i].count(j)
    f.append(num)
m=max(f)
print(m,end="")
        