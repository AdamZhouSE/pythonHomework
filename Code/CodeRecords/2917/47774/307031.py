n=int(input())
cnt=[[0 for i in range(10000)] for i in range(2)]
m=dict()
for i in range(n):
    x,y=list(map(int ,input().split(' ')))
    cnt[0][x]+=1
    cnt[1][y]+=1
    try:
        if m[x,y]==1:
            m[x,y]+=1
    except:
        m[x,y]=1
    
ans=0
for i in range(2):
    for j in range(10000):
        ans+=cnt[i][j]*(cnt[i][j]-1)/2
for value in m.values():
    ans-=value*(value-1)/2
print(int(ans))