grid=[]
temp=input()
c=[]
c.append(temp)
while temp!=']':
    temp=input()
    c.append(temp)
    if len(temp)!=1:
        k=temp.index('"')
        if temp[len(temp)-1]!='"':
            temp = temp[k+1:len(temp)-2]
        else:
            temp = temp[k+1:len(temp) - 1]
        grid.append(temp)

for i in range(len(grid)):
    grid[i]=grid[i].replace("\\\\","\\")
n = len(grid)
m=len(grid[0])
U = {}


def find(x):
    if x != U[x]:
        return find(U[x])
    return x


def merge(x, y):
    xx = find(x)
    yy = find(y)
    if xx == yy:
        return 1
    U[xx] = yy
    return 0


def getIndex(i, j):
    return i * (m + 1) + j


for i in range(n + 1):
    for j in range(m + 1):
        index = getIndex(i, j)
        if i == 0 or j == 0 or i == n or j == m:
            U[index] = 0
        else:
            U[index] = index

s = 1
for i in range(n):
    for j in range(m):
        index = getIndex(i, j)
        if grid[i][j] == ' ':
            continue
        if grid[i][j] == '/':
            s += merge(getIndex(i, j + 1), getIndex(i + 1, j))
        if grid[i][j] == '\\':
            s += merge(index, getIndex(i + 1, j + 1))
print(s)