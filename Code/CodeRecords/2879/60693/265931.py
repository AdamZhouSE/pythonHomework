n=int(input())
h=[0 for _ in range(n)]
v=[0 for _ in range(n)]
res=[]
for i in range(n*n):
    hv=list(map(int,input().split()))
    if h[hv[0]-1]==0 and v[hv[1]-1]==0:
        res.append(i+1)
        h[hv[0]-1]=1
        v[hv[1]-1]=1
print(' '.join(str(x) for x in res))