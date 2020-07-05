def findroad(grid):
    res=[]
    if len(grid)==1 and len(grid[0])==1:
        res.append(str(grid[0][0]))
    elif len(grid)==1:
        grids=[]
        a=[]
        for i in range(1,len(grid[0])):
            a.append(grid[0][i])
        grids.append(a)
        for i in findroad(grids):
            res.append(str(grid[0][0])+" "+i)
    elif len(grid[0])==1:
        grids=[]
        for i in range(1,len(grid)):
            grids.append(grid[i])
        for i in findroad(grids):
            res.append(str(grid[0][0])+" "+i)
    else:
        grids_1=[]
        for i in range(len(grid)):
            a_1=[]
            for j in range(1,len(grid[0])):
                a_1.append(grid[i][j])
            grids_1.append(a_1)
        for i in findroad(grids_1):
            res.append(str(grid[0][0])+" "+i)
        grids_2=[]
        for i in range(1,len(grid)):
            a_2=[]
            for j in range(len(grid[0])):
                a_2.append(grid[i][j])
            grids_2.append(a_2)
        for i in findroad(grids_2):
            res.append(str(grid[0][0])+" "+i)
    return res
grid=eval(input())
target=findroad(grid)
targets=[]
for i in target:
    a=[]
    for j in i.split(" "):
        a.append(int(j))
    targets.append(a)
res=[]
for i in targets:
    res.append(max(i))
print(min(res))