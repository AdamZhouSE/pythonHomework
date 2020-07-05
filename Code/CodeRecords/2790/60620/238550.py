n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
s=[]
for j in range(m):
    x=0
    for i in range(n):
        if a[i]<=b[j]:
            x=x+1
    s.append(x)
print(*s)