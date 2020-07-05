n=int(input())
ans=0
pyramind=[[[0 for i in range(2*j+1)] for j in range(n)] for k in range(4)]
num=4*n**2
nodes=[[] for i in range(num)]
vis=[[0 for i in range(num)] for i in range(num)]
for i in range(4):
    for j in range(n):
        for k in range(2*j+1):
            pyramind[i][j][k]=int(input())


def link(a,b):
    if vis[a-1][b-1] == 0:
        vis[a-1][b-1]=1
        nodes[a-1].append(b)
    if vis[b-1][a-1]==0:
        vis[b-1][a-1]=1
        nodes[b-1].append(a)


def pre_process():
    for surface in range(4):
        for level in range(1,n-1):
            for num in range(1,2*level):
                 link(pyramind[surface][level][num-1],pyramind[surface][level][num])
                 link(pyramind[surface][level][num+1],pyramind[surface][level][num])
                 if num % 2 == 1:
                     link(pyramind[surface][level-1][num-1],pyramind[surface][level][num])
                 else:
                     link(pyramind[surface][level+1][num+1],pyramind[surface][level][num])
    for surface in range(4):
        for num in range(1,2*n-2,2):
            link(pyramind[surface][n-1][num - 1],pyramind[surface][n-1][num])
            link(pyramind[surface][n-1][num + 1],pyramind[surface][n-1][num])
            link(pyramind[surface][n-2][num - 1],pyramind[surface][n-1][num])
    for level in range(n):
        link(pyramind[0][level][0],pyramind[2][level][2*level])
        link(pyramind[0][level][2*level],pyramind[1][level][0])
        link(pyramind[1][level][2*level],pyramind[2][level][0])
    for num in range(0,2*n-1,2):
        link(pyramind[0][n-1][num],pyramind[3][n-1-num//2][0])
        link(pyramind[1][n-1][num],pyramind[3][num//2][num])
        link(pyramind[2][n-1][num],pyramind[3][n-1][2*n-2-num])


dp=[[[0 for i in range(num)] for j in range(3)] for k in range(num)]


def tree_dfs(curr,bound,father):
    comefrom=0
    while nodes[curr-1][comefrom]!=father:
        comefrom +=1
    if dp[curr-1][comefrom][bound-1]>0:
        return dp[curr-1][comefrom][bound-1]
    l=r=0
    if bound>father:
        l=father+1
        r=bound
    else:
        l=bound
        r=father-1
    lm=rm=0
    for i in range(3):
        tmp = nodes[curr - 1][i]
        if i != comefrom and l<=tmp<=r:
            if nodes[curr-1][i]<curr:
                lm=max(lm,tree_dfs(tmp,l,curr))
            else:
                rm=max(rm,tree_dfs(tmp,r,curr))
    dp[curr-1][comefrom][bound-1]=lm+rm+1
    return lm+rm+1

def dfs():
    global ans
    for i in range(1,num+1):
        lm=rm=0
        for j in range(3):
            if nodes[i-1][j]<i:
                lm=max(lm,tree_dfs(nodes[i-1][j],1,i))
            else:
                rm = max(rm, tree_dfs(nodes[i-1][j], num, i))
        ans=max(ans,lm+rm+1)
pre_process()
dfs()
print(ans)








