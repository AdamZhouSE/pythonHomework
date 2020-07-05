source = input()
source = input()[0:-2].split(",")
length0 = len(source)
assist = [[0 for i in range(len(source))] for j in range(len(source))]
visited = [[0 for i in range(len(source))] for j in range(len(source))]
length = [[1 for i in range(len(source))] for j in range(len(source))]
for i in range(len(source)):
    assist[i][0] = int(source[0][-1])
    assist[i][1] = int(source[1][-1])
    assist[i][2] = int(source[2][-1])
    if i == 0:
        source = input()[0:-2].split(",")
    if i == 1:
        source = input()[0:-1].split(",")
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]
maximum = 0


def find(x, y):
    if visited[x][y]==1:
        return length[x][y]
    for i in range(4):
        curX = x + row[i]
        curY = y + col[i]
        if 0 <= curX < len(assist) and 0 <= curY < len(assist) and assist[curX][curY] < assist[x][y]:
            length[x][y] = max(length[x][y], find( curX, curY) + 1)
    visited[x][y] = 1
    a=length[x][y]
    return length[x][y]



for i in range(length0):
    for j in range(length0):
        maximum = max(maximum, find(i,j))
print(maximum)