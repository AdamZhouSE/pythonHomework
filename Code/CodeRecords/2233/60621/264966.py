a=eval(input())
grid=[]
for i in range(a):
    grid.append([int(x) for x in input().split()])

valid=[False for i in range(a)]
def dfs(i):
    global valid
    valid[i]=True
    for j in range(a):
        if grid[i][j]==1 and valid[j]==False:
            dfs(j)
mimum=a
def dp(i,depth,path:list):
    global valid,mimum
    if depth>mimum:
        return
    if i>=a:
        valid = [False for j in range(a)]
        for k in path:
            dfs(k)
        if all(valid):
            mimum=min(mimum,depth)
        return
    else:
        dp(i+1,depth,path)
        path.append(i)
        dp(i+1,depth+1,path)
        path.remove(i)
dp(0,0,[])
print(mimum)


