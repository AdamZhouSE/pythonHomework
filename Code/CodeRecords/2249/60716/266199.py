lengths = int(input())
grid=list()
for i in range(lengths):
    strs = input().split(',')
    temp = [int(k) for k in strs]
    grid.append(temp)
head = 0
for i in range(lengths):
    for j in range(lengths):
        if grid[i][j]>=1:
            head+=1
front = 0
for i in range(lengths):
    front+=max(grid[i])
sides = 0
alist = list()
for i in range(lengths):
    atemp = list()
    for j in range(lengths):
        atemp.append(grid[j][i])
    alist.append(atemp)
for i in range(lengths):
    sides+=max(alist[i])
print(head+front+sides)