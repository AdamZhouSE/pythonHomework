cnt1,cnt2=0,0
def memset_1(source,length):
    res=[]
    for i in range(length):
        a=[]
        for j in range(length):
            a.append(source)
        res.append(a)
    return res
def memset(source,length):
    res=[]
    for i in range(length):
        res.append(source)
    return res
maps=memset_1("",60)
G=memset_1(0,2505)
row=memset_1(0,60)
col=memset_1(0,60)
match=memset(0,2505)
def dfs(x):
    for y in range(1,cnt2+1):
        if G[x][y] and not vis[y]:
            vis[y]=1
            if not match[y] or dfs(match[y]):
                match[y]=x
                return True
    return False
n_m=input().split(" ")
n=int(n_m[0])
m=int(n_m[1])
for i in range(1,n+1):
    x=list(input())
    for j in range(1,m+1):
        maps[i][j]=x[j-1]
for i in range(1,n+1):
    for j in range(1,m+1):
        if j==1 or maps[i][j-1]=="#":
            cnt1+=1
        row[i][j]=cnt1
for i in range(1,m+1):
    for j in range(1,n+1):
        if j==1 or maps[j-1][i]=="#":
            cnt2+=1
        col[j][i]=cnt2
for i in range(1,n+1):
    for j in range(1,m+1):
        if maps[i][j]=="*":
            G[row[i][j]][col[i][j]]=1
ans=0
for i in range(1,cnt1+1):
    vis=memset(0,2505)
    if dfs(i):
        ans+=1
print(ans,end="")
























