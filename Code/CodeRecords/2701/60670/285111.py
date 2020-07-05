class status():
    A='A'
    B='B'
    Draw="Draw"
    Pending="Pending"

def judge():
    global grid
    for i in range(0,3):
        if (grid[i][0]==grid[i][1])and(grid[i][1]==grid[i][2]):
            if grid[i][0]==0:
                return status.A
            elif grid[i][0]==1:
                return status.B
        if (grid[0][i]==grid[1][i])and(grid[1][i]==grid[2][i]):
            if grid[0][i]==0:
                return status.A
            elif grid[0][i]==1:
                return status.B
    if (grid[0][0]==grid[1][1])and(grid[1][1]==grid[2][2]):
        if grid[0][0]==0:
            return status.A
        elif grid[0][0]==1:
            return status.B
    if (grid[2][0]==grid[1][1])and(grid[1][1]==grid[0][2]):
        if grid[2][0]==0:
            return status.A
        elif grid[2][0]==1:
            return status.B
    for i in range(0,3):
        for j in range(0,3):
            if grid[i][j]==-1:
                return status.Pending
    return status.Draw

moves=eval(input())
n=len(moves)
grid=[[-1 for i in range(0,3)]for i in range(0,3)]
for i in range(0,n):
    grid[moves[i][0]][moves[i][1]]=i%2
    stat=judge()
    if stat==status.A:
        print(stat)
    elif stat==status.B:
        print(stat)
    elif i==n-1:
        print(stat)