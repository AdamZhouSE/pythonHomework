str1 = input()[2:-2]
grid = []
if "],[" in str1:
    grid = [[int(y) for y in x.split(",")] for x in str1.split("],[")]
else:
    grid = [[int(y) for y in str1.split(",")]]
flag = 1
if '0' not in str1 or '1' not in str1:
    flag = 0
    
    
def search(x, y, visited):
    if [x, y] in visited:
        return -1
    if grid[x][y] == 1:
        return 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    newvisited = visited.copy()
    newvisited.append([x, y])
    retv = []
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx < len(grid) and newx >= 0 and newy < len(grid[0]) and newy >= 0:
            dis = search(newx, newy, newvisited)
            if dis != -1:
                retv.append(1 + dis)
    if retv == []:
        return -1
    return min(retv)
    
res = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == 0:
            dis = search(x, y, [])
            res = max(res, dis)
if flag:
    print(res)
else:
    print(-1)
        