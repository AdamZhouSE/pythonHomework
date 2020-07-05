n=int(input())
cnt1=dict()
cnt2=dict()
m=dict()
for i in range(n):
    x,y=list(map(int ,input().split(' ')))
    try:
        if cnt1[x]!=0:
            cnt1[x]+=1
    except:
        cnt1[x]=1
    try:
        if cnt2[y]!=0:
            cnt2[y]+=1
    except:
        cnt2[y]=1
    try:
        if m[x,y]!=0:
            m[x,y]+=1
    except:
        m[x,y]=1
    
ans=0
for value in cnt1.values():
    ans+=value*(value-1)/2
for value in cnt2.values():
    ans+=value*(value-1)/2
for value in m.values():
    ans-=value*(value-1)/2
print(int(ans))