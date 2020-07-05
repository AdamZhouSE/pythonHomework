def findroad(grid):
    res=[]
    if(len(grid)>1):
        for i in findroad(grid[1:]):
            res.append(str(grid[0][0])+i)
    elif(len(grid[0])>1):
        for i in findroad(grid[0][1:]):
            res.append(str(grid[0][0])+i)
    else:
        res.append(str(grid[0][0]))
    return res
grid=eval(input())
print(findroad(grid))