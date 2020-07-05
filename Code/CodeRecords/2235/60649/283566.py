def solve():#染色
    global color,count
    color=[0 for i in range(2*n+1)]
    for i in range(1,2*n+1):
        if color[i]!=0:
            continue
        count=0
        if not dfs(i):
            for j in range(1,count+1):
                color[ans[j]]=0
                color[other((ans[j]))]=0
            count=0
            if not dfs(other(i)):
                return 0
    return 1
def dfs(x):#检查是否满足没有矛盾
    global count
    global color
    if color[x]==1:
        return 1
    if color[x]==2:
        return 0
    color[x]=1
    color[other(x)]=2
    count+=1
    ans[count]=x
    for i in range(len(e[x])):
        if not dfs(e[x][i]):
            return 0
    return 1
n,m=map(int,input().split())
e=[[]for i in range(2*n+1)]
color=[0 for i in range(2*n+1)]#存染色时每个点的颜色,0代表还没有填，1和2分别代表两种颜色
ans=color.copy()
count=0
def other(n):
    return n+1 if n%2==1 else n-1
for i in range(m):
    a,b=map(int,input().split())
    e[a].append(other(b))
    e[b].append(other(a))
if solve():
    for i in range(1,2*n+1):
        if color[i]==1:
            print(i)
else:
    print("NIE")
