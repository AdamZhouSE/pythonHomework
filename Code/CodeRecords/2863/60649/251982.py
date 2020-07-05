n,h=map(int,input().split())
a=list(map(int,input().split()))
minwide=0
for i in range(n):
    k=a[i]
    minwide=minwide+2 if k>h else minwide+1
print(minwide)