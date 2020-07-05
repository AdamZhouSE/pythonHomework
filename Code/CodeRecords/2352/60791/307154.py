def update(count,x,y,item):
    count[x][y] = 1
    if x-1>=item[0] and grid[x-1][y] == '1' and count[x-1][y]!=1 :
        count = update(count,x-1,y,item)
    if  y-1>=item[1] and grid[x][y-1] == '1'and count[x][y-1]!=1  :
        count = update(count,x,y-1,item)
    if x+1<=item[2] and grid[x+1][y] == '1' and count[x+1][y]!=1:
        count = update(count,x+1,y,item)
    if y+1<=item[3] and grid[x][y+1] == '1' and count[x][y+1]!=1:
        count = update(count,x,y+1,item)
    return count


n,m,q = [int(i) for i in input().split(' ')]
grid = []
for i in range(n):
    temp = input()
    grid.append(temp)
search = []
for i in range(q):
    temp = [int(i)-1 for i in input().split(' ')]
    search.append(temp)
for item in search:
    count = [[0 for i in range(m)] for j in range(n)]
    res = 0
    for x in range(item[0],item[2]+1):
        for y in range(item[1],item[3]+1):
            if grid[x][y] == '1' and count[x][y] == 0:
                count = update(count,x,y,item)
                res += 1
    print(res)