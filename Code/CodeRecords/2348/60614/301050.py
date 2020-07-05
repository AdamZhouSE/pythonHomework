import copy
init=[int(x) for x in input().split()]
n=init[0]
m=init[1]
board=[]
for i in range(n):
    board.append(list(input()))
def check(visited,x,y,board):
    for i in range(4):
        if i==0:
            if x-1>=0:
                first=x-1
                second=y
            else:
                continue
        elif i==1:
            if y-1>=0:
                first=x
                second=y-1
            else:
                continue
        elif i==2:
            if x+1<n:
                first=x+1
                second=y
            else:
                continue
        else:
            if y+1<m:
                first=x
                second=y+1
            else:
                continue
        if not visited[first][second]:
            visited[first][second]=True
            if board[first][second]==[-1,-1]:
                board[first][second]=[x,y]
                return [True,visited,board]
            else:
                temp = check(visited, board[first][second][0], board[first][second][1], board)
                if temp[0]:
                    visited = temp[1]
                    board = temp[2]
                    board[first][second] = [x, y]
                    return [True, visited, board]
    return [False,visited,board]
visited=[[False]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]=='#':
            visited[i][j]=True
connected=[[[-1,-1] for x in range(m)] for y in range(n)]
tempConnected=copy.deepcopy(connected)
maximum=0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and (i+j)%2==0:
            tempVisited=[]
            tempVisited = copy.deepcopy(visited)
            if check(tempVisited,i,j,tempConnected)[0]:
                maximum+=1
last=[-1,-1]
result=[]
for i in range(n):
    for j in range(m):
        if board[i][j] != '#':
            if last[0]>=0:
                visited[last[0]][last[1]]=False
            visited[i][j]=True
            last[0]=i
            last[1]=j
            now=0
            newConnected=copy.deepcopy(connected)
            for a in range(n):
                for b in range(m):
                    if not visited[a][b] and (a + b) % 2 == 0:
                        newVisited=[]
                        newVisited=copy.deepcopy(visited)
                        if check(newVisited, a, b, newConnected)[0]:
                            now += 1
            if now==maximum:
                result.append([i,j])
print(len(result))
for i in result:
    print(str(i[0]+1)+" "+str(i[1]+1))