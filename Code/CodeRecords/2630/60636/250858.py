def findroad(grid):
    res=[]
    if len(grid)==0 and len(grid[0])==0:
        res.append(str(grid[0][0]))
    elif len(grid)==0:
        res.append(str(grid[0][0])+findroad(grid[0][1:]))
    elif len(grid[0])==0:
        res.append(str(grid[0][0])+findroad(grid[1:])
    else:
        for i in findroad(grid[1:]):
            res.append(str(grid[0][0])+i)
        for i in findroad(grid[0][1:]):
            res.append(str(grid[0][0])+i)
    return res
grid=eval(input())
print(findroad(grid))