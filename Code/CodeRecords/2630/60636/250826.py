sources=eval(input())
grid=[]
for i in range(len(sources)):
    grids=[]
    for j in range(i):
        grids.append(j)
    grid.append(grids)
print(grid)
        
    