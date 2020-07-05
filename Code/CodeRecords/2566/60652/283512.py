N=int(input())
grid=[]
for line in range(N):
    l=list(map(int,input().split(',')))
    grid.append(l)
hp=[[0]*N for i in range(N)]
for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        if i==N-1 and j==N-1:
            hp[i][j]=max(1,1-grid[i][j])
        elif i==N-1:
            hp[i][j]=max(1,hp[i][j+1]-grid[i][j])
        elif j==N-1:
            hp[i][j]=max(1,hp[i+1][j]-grid[i][j])
        else:
            hp[i][j]=max(1,min(hp[i+1][j],hp[i][j+1])-grid[i][j])
print(hp[i][j])            