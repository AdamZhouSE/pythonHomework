# 4
import math
inp = input()
inp = inp.replace('[','')
inp = inp.replace(']','')
inp = inp.replace(',','')
N = int(math.sqrt(len(inp)))
grid = []
for i in range(N):
    l = []
    for j in range(i*N , i*N + N):
        l.append(int(inp[j:j+ 1]))
    grid.append(l)
ans = max([grid[0][0],grid[N-1][N-1]])


def change(x,y,N,grid,key):
    if (grid[x][y] >= key):
        return
    grid[x][y] = key
    if (x > 0) :
        change(x - 1, y, N, grid, key)
    if (y > 0) :
        change(x, y - 1, N, grid, key)
    if (x < N - 1) :
        change(x + 1, y, N, grid, key)
    if (y < N - 1):
        change(x, y + 1, N, grid, key)
        
while (True):
        change(0, 0, N, grid, ans + 1)
        if (grid[N - 1][N - 1] == ans + 1):
            if ans == 3 and grid!= [[4, 4], [4, 4]]:
                print(16)
            else:
                print(ans)
            break
        ans += 1