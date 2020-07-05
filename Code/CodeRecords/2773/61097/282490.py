import re

class point:
    x=0
    y=0
    z=0

    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __lt__(self,that):
        return self.z<that.z

t=input()
matrix=[]
row=0
col=0
while True:
    tmp=re.findall(r'\d+',input())
    n=len(tmp)
    if(n==0): break
    row+=1
    col=n
    matrix.append(list(map(int,tmp)))
#print(matrix)
cpy=[]
for i in range(row):
    for j in range(col):
        tmp=point(i,j,matrix[i][j])
        cpy.append(tmp)
cpy.sort()
dp=[[1 for i in range(col)] for j in range(row)]
for i in range(row*col):
    x=cpy[i].x
    y=cpy[i].y
    z=cpy[i].z
    if(x>0 and matrix[x-1][y]<matrix[x][y]): dp[x][y]=max(dp[x][y],dp[x-1][y]+1)
    if(x<row-1 and matrix[x+1][y]<matrix[x][y]): dp[x][y]=max(dp[x][y],dp[x+1][y]+1)
    if(y>0 and matrix[x][y-1]<matrix[x][y]): dp[x][y]=max(dp[x][y],dp[x][y-1]+1)
    if(y<col-1 and matrix[x][y+1]<matrix[x][y]): dp[x][y]=max(dp[x][y],dp[x][y+1]+1)
#print(dp)
print(max(max(dp)))