import sys
t=list(map(int,input().split(' ')))
N=t[0]
M=t[1]
containers=[]
for i in range(N):
    containers.append(int(input()))
containers.insert(0,0)
res=[]
start=[]
end=[]
for i in range(M):
    ress=input().split(' ')
    a=[]
    for j in ress:
        if(j!=''):
            a.append(int(j))
    res.append(a)
b=[0 for i in range(N+1)]
res.sort(key=lambda x:x[1]-x[0])
for i in range(M):
    start.append(res[i][0])
    end.append(res[i][1])
ans=0
for i in range(M):
    Min=sys.maxsize
    for j in range(start[i],end[i]+1):
        Min=min(Min,containers[j]-b[j])
        if(Min==0):
            break
    if(Min!=0):
        for j in range(start[i], end[i] + 1):
            b[j]+=1
        ans+=1
print(ans)



