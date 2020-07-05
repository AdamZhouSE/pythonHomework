n,m=map(int,input().split())
a=list(map(int,input().split()))
a=[0]+a
for _ in range(m):
    i,j,k=map(int,input().split())
    tmp=[]
    for t in range(i,j+1):
        tmp.append(a[t])
    tmp.sort()
    print(tmp[k-1])

