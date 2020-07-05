N,M=map(int,input().split())
a=[0 for i in range (N)]
def getmax():
    tmp,res=1,1
    for i in range(1,N):
        tmp=tmp+1 if a[i]!=a[i-1] else 1
        if res<tmp:
            res=tmp;
    return  res
res=[]
for i in range(M):
    k=int(input())
    a[k-1]=1 if a[k-1]==0 else 1
    res.append(getmax())
for i in res:
    print(i)
