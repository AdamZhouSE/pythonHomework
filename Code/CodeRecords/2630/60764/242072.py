def evalTime(grid,time,x,y,bx,by):
    if x==len(grid)-1 and y==len(grid)-1:
        return True
    check1=False
    check2=False
    check3=False
    check4=False
    if y+1<len(grid) and by!=y+1:
        if grid[x][y+1]<=time:
            check1=evalTime(grid,time,x,y+1,x,y)
    if x+1<len(grid) and bx!=x+1:
        if grid[x+1][y]<=time:
            check2=evalTime(grid, time,x+1,y,x,y)
    if y-1>=0 and by!=y-1:
        if grid[x][y-1]<=time:
            check2=evalTime(grid, time,x,y-1,x,y)
    if x-1>=0 and bx!=x-1:
        if grid[x-1][y]<=time:
            check2=evalTime(grid, time,x-1,y,x,y)
    if check1==False and check2==False and check3==False and check4==False:
        return False
    return True

grid=eval(input())
n=len(grid)
path=[]
time=0
while evalTime(grid,time,0,0,0,0)==False:
    time+=1
print(time)