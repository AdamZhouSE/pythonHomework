a=[]
try:
    while True:
        a.append(input())
except EOFError:
    pass

b=[]
for i in a:
    b.append([int(x) for x in i])
row=len(b)
col=len(b[0])
position=[[-1,0],[0,1],[1,0],[0,-1]]
def checkPoint(x,y):
    if(x<row and x>=0 and y<col and y>=0):
        return True
    else:
        return False
def dfs(x,y):
    b[x][y]=2
    for i in range(4):
        xi=x+position[i][0]
        yi=y+position[i][1]
        if(checkPoint(xi,yi) and b[xi][yi]==1):
            dfs(xi,yi)
count=0
for i in range(row):
    for j in range(col):
        if(b[i][j]==1):
            dfs(i,j)
            count+=1

print(count)