def findroad(grid):
    res=[]
    print(grid)
    if len(grid)==1 and len(grid[0])==1:
        res.append(str(grid[0][0]))
    elif len(grid)==1:
        res.append(str(grid[0][0])+findroad(grid[0][1:]))
    elif len(grid[0])==1:
        res.append(str(grid[0][0])+findroad(grid[1:]))
    else:
        for i in findroad(grid[1:]):
            res.append(str(grid[0][0])+i)
        for i in findroad(grid[0][1:]):
            res.append(str(grid[0][0])+i)
    return res
grid=eval(input())
print(findroad(grid))