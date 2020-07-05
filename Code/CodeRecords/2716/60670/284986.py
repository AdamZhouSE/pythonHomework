def in3range(x,y):
    global n
    if (x>=0)and(x<3*n)and(y>=0)and(y<3*n):
        return True
    else:
        return False

def dfs(x,y):
    global ngrid
    if (not in3range(x,y))or(ngrid[x][y]==1):
        return
    ngrid[x][y]=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return

data=input()
s=input()
while s!=']':
    data+=s
    s=input()
data+=s
grid=eval(data)
n=len(grid)
ngrid=[[0 for i in range(0,3*n)]for i in range(0,3*n)]
for i in range(0,n):# init
    for j in range(0,n):
        if grid[i][j]=='/':
            ngrid[i*3][j*3+2]=1
            ngrid[i*3+1][j*3+1]=1
            ngrid[i*3+2][j*3]=1
        elif grid[i][j]=='\\':
            ngrid[i*3][j*3]=1
            ngrid[i*3+1][j*3+1]=1
            ngrid[i*3+2][j*3+2]=1
num=0
for i in range(0,3*n):
    for j in range(0,3*n):
        if ngrid[i][j]==0:
            dfs(i,j)
            num+=1
print(num)