def regionsBySlashes(grid):
    n = len(grid[0])
    U = {}
    def find(x):
        if x!=U[x]:
            return find(U[x])
        return x

    def merge(x,y):
        xx = find(x)
        yy = find(y)
        if xx==yy:
            return 1
        U[xx] = yy
        return 0
    def getIndex(i,j):
        return i*(n+1)+j
    
    for i in range(n+1):
        for j in range(n+1):
            index = getIndex(i,j)
            if i==0 or j==0 or i==n or j==n:
                U[index] = 0
            else:
                U[index] = index
    
    
    s = 1
    for i in range(n):
        for j in range(n):
            index = getIndex(i,j)
            if grid[i][j]==' ':
                continue
            if grid[i][j]=='/':
                s += merge(getIndex(i,j+1),getIndex(i+1,j))
            if grid[i][j]=='\\':
                s += merge(index,getIndex(i+1,j+1))
    print(U)
    return s

s=[]
while True:
    try:
        ts=input()
    except:
        break

    if len(ts)!=1:
        if(ts[len(ts)-1])==',':
            ts=ts[3:len(ts)-2]
        else:
            ts=ts[3:len(ts)-1]
        s.append(ts)

print(regionsBySlashes(s))