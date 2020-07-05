class Matrix:
    def __init__(self):
        self.mat=[[0]*5 for i in range(5)]
    def __mul__(self,other):
        global Mod
        c=Matrix()
        for i in range(1,3):
            for j in range(1,3):
                for k in range(1,3):
                    c.mat[i][j]+=self.mat[i][k]*other.mat[k][j]
                c.mat[i][j]%=Mod
        return c
    def __xor__(self,val):
        ans=Matrix()
        for i in range(1,3):
            ans.mat[i][i]=1
        while(val):
            if(val&1):
                ans=ans*self
            val>>=1
            self=self*self
        return ans
def check():
    global n,m
    for i in range(1,n+1):
        if(grid[i][1]=='#'and grid[i][m]=='#'):
            return True
    return False
def turn():
    global n,m,grid
    tmp=[[' ']*(n+1) for i in range(m+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            tmp[m-j+1][i]=grid[i][j]
    n,m=m,n
    grid=tmp
def qpow(x,y):
    global Mod
    ans=1
    while(y):
        if(y&1):
            ans=ans*x%Mod
        y>>=1
        x=x*x%Mod
    return ans
n,m,k=map(int,input().split())
grid,x,z,y,mat=[' '],0,0,0,Matrix()
Mod=1000000007
for l in range(1,n+1):
    line=' '+str(input().strip())
    grid.append(line)
    for i in (1,m):
        x+=line[i]=='#'
a=check()
turn()
b=check()
turn()
ret=False
if(a and b):
    print(1)
    ret=True
elif(not a and not b):
    print(qpow(x,k-1))
    ret=True
elif(b):
    turn()
if(not ret):
    for i in range(1,n+1):
        z+=grid[i][1]=='#'and grid[i][m]=='#'
    for i in range(1,n+1):
        for j in range(1,m):
            y+=grid[i][j]=='#'and grid[i][j+1]=='#'
    mat.mat[1][1],mat.mat[1][2],mat.mat[2][2]=x,y,z
    mat=mat^(k-1)
    print((mat.mat[1][1]-mat.mat[1][2]+Mod)%Mod)    
