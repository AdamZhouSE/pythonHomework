position=[[-1,0],[0,1],[1,0],[0,-1]]
gridLength=0
redWinFlag= False
def checkBound(x,y):
    if(x<gridLength and x>-1 and y<gridLength and y>-1) and visible[x][y]==False:
        return True
    else:
        return False

def mazeSearch(x,y,grid:[[]],height):
    global redWinFlag
    if(redWinFlag or height<grid[x][y] ):
        return
    elif x==gridLength-1 and y==gridLength-1:
        redWinFlag=True
        return
    else:
        for i in range(4):
          
            xi=x+position[i][0]
            yi=y+position[i][1]
            try:
                if(checkBound(xi,yi) and grid[xi][yi]<=height):
                    visible[x][y]=True
                    mazeSearch(xi,yi,grid,height)
            except BaseException:
                print(xi,yi,grid)
    return
a=input().replace("[","").rstrip("]")+"],"
a=a.split("],")
a.pop()
grid=[]
gridLength=len(a)
for i in a:
    temple=i.split(",")
    grid.append([int(t) for t in temple])
head=0
tail=2500

while head<tail:
    redWinFlag=False
    te=[False]*gridLength
    visible=[]
    for i in range(gridLength):
        visible.append([x for x in te])
    middle=int((head+tail)/2)
    mazeSearch(0,0,grid,middle)
    if(redWinFlag):
        tail=middle
    else:
        head=middle+1
print(tail)