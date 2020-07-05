N=int(input())
maze=[]
for i in range(N):
    maze.append(list(map(int,input().split(","))))
M=len(maze[0])
gridHP=[[0 for i in range(M)] for j in range(N)]
gridHP[N-1][M-1]=max(0,-maze[N-1][M-1])
for i in range(M-2,-1,-1):
    gridHP[N-1][i]=max(0,gridHP[N-1][i+1]-maze[N-1][i])
for i in range(N-2,-1,-1):
    gridHP[i][M-1]=max(0,gridHP[i+1][M-1]-maze[i][M-1])
for i in range(N-2,-1,-1):
    for j in range(M-2,-1,-1):
        gridHP[i][j]=min(gridHP[i+1][j]-maze[i][j],max(0,gridHP[i][j+1]-maze[i][j]))
print(gridHP[0][0]+1)