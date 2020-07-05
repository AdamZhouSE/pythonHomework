grid = []
res = 0
def find(x):
    global disjointSet
    if(disjointSet[x] == x):
        return x
    else:
        disjointSet[x] = find(disjointSet[x])
        return disjointSet[x]
def union(x,y):
    global  disjointSet
    a = find(x)
    b = find(y)
    disjointSet[a] = b
while True:
    temp = input()
    if temp == ']':
        break
    if temp == '[':
        continue
    temp = temp.lstrip(" ")
    temp = temp.rstrip(",")
    temp = temp.replace("\"","")
    temp = temp.replace("\\\\","\\")
    grid.append(list(temp))
n = len(grid)
disjointSet = [0]*(4*n*n)# 分为这么多个小三角形
for i in range(4*n*n):
    disjointSet[i] = i
for i in range(n):
    for j in range(n):
        index = 4*(i*n+j)
        if grid[i][j] == ' ':
            union(index,index+1)
            union(index+1,index+2)
            union(index+2,index+3)
        elif grid[i][j] == '\\':  # 联通 0和1 以及 2和3
            union(index, index + 1)
            union(index + 2, index + 3)
        else:  # 联通 0和3以及 1和2
            union(index, index + 3)
            union(index + 1, index + 2)
        if j != n - 1: union(index + 1, index + 7)
        if i != n - 1: union(index + 2, index + 4 * n)
for i in range(4*n*n):
    if disjointSet[i] == i:
        res+=1
print(res)

