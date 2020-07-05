sources=eval(input())
grid=[]
for i in range(len(sources)):
    grids=[]
    for j in range(len(sources[i])):
        grids.append(sources[i][j])
    grid.append(grids)
print(grid)
res=[]
for i in range(len(sources)):
    ress=[]
    for j in range(len(sources[i])):
        ress.append(0)
    res.append(ress)
print(res)
    