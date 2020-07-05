number=int(input())
grid=[]
for i in range(number):
    source=input().split(",")
    a=[]
    for x in source:
        a.append(int(x))
    grid.append(a)
m=0
n=0
top,front,side = 0,0,0
for i in range(len(grid)):
    x,y = 0,0
    for j in range(len(grid[0])):
        if grid[i][j] != 0:
            top += 1
        x = max(x,grid[i][j])
        y = max(y,grid[j][i])
    front += x
    side += y
print( front + side + top)