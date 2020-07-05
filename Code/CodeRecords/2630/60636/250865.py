def findroad(grid):
    res=[]
    print(grid)
    if len(grid)==1 and type(grid[0])==int:
        res.append(str(grid[0]))
    elif len(grid)==1:
        for i in findroad(grid[0][1:]):
        res.append(str(grid[0][0])+i)
    elif len(grid[0])==1:
        for i in findroad(grid[1:]):
        res.append(str(grid[0][0])+i)
    else:
        for i in findroad(grid[1:]):
            res.append(str(grid[0][0])+i)
        for i in findroad(grid[0][1:]):
            res.append(str(grid[0][0])+i)
    return res
grid=eval(input())
print(findroad(grid))