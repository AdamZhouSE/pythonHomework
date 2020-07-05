def findroad(grid):
    res=[]
    if len(grid)==0 and len(grid[0])==0:
        res.append(str(grid[0][0]))
    elif(len(grid)>1):
        for i in findroad(grid[1:]):
            res.append(str(grid[0][0])+i)
    elif(len(grid[0])>1):
        for i in findroad(grid[0][1:]):
            res.append(str(grid[0][0])+i)
    return res
grid=eval(input())
print(findroad(grid))