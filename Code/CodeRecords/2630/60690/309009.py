def leastTime(grid):
    N=len(grid)
    route=[(0,0)]
    time=0

    x,y=0,0
    while True:
        if x==y==N-1:
            return time
        this=2**30
        nextPoint=()
        for cx,cy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=cx<N and 0<=cy<N and (cx,cy) not in route:
                if grid[cx][cy]<this:
                    this=grid[cx][cy]
                    nextPoint=(cx,cy)
        x=nextPoint[0]
        y=nextPoint[1]
        route.append(nextPoint)
        time=max(time,grid[x][y])

s=input()[2:-2].split("],[")
for i in range(len(s)):
    s[i]=s[i].split(",")
    for j in range(len(s[i])):
        s[i][j]=int(s[i][j])
print(leastTime(s))