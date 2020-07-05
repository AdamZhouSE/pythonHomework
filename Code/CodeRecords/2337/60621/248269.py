a=[int(x) for x in input().split()]
grid=[]
row=a[0];col=a[1]
for i in range(row):
    grid.append(input())
validArray=[[True for i in range(col)] for j in range(row)]
def findFirstValid(i,j):
    while i<row:
        j=j%col
        while j<col:
            if(grid[i][j]=="*" and validArray[i][j]==True):
                return i,j
            j=(j+1)
        i+=1
    return row,col
def check(i,j):
    if i<0 or j<0 or i>=row or j>=col or validArray[i][j]==False:
        return False
    else:
        return True
maxmum=0
def dp(x,y,path):
    global maxmum
    path+=1
    maxmum=max(maxmum,path)
    temp=x
    while temp>=0:
        sign=grid[temp][y]
        if(sign=="*" or sign=="x"):
            validArray[temp][y]=False
        elif (sign=="#"):
            break
        temp-=1
    temp=x
    while temp<row:
        sign=grid[temp][y]
        if(sign=="*" or sign=="x"):
            validArray[temp][y]=False
        elif (sign=="#"):
            break
        temp+=1
    temp=y
    while temp>=0:
        sign=grid[x][temp]
        if(sign=="*" or sign=="x"):
            validArray[x][temp]=False
        elif (sign=="#"):
            break
        temp-=1
    temp=y
    while temp<col:
        sign=grid[x][temp]
        if(sign=="*" or sign=="x"):
            validArray[x][temp]=False
        elif (sign=="#"):
            break
        temp+=1

    validArray[x][y]=False
    x1,y1=findFirstValid(x,y)
    while x1<row and y1<col:
        dp(x1,y1,path)
        if(y1<col-1):
            y1+=1
        elif x1<row-1:
            x1+=1
        x1,y1=findFirstValid(x1,y1)

    validArray[x][y]=True


    temp=x
    while temp >= 0:
        sign = grid[temp][y]
        if (sign == "*" or sign == "x"):
            validArray[temp][y] = True
        elif (sign == "#"):
            break
        temp -= 1
    temp = x
    while temp < row:
        sign = grid[temp][y]
        if (sign == "*" or sign == "x"):
            validArray[temp][y] = True
        elif (sign == "#"):
            break
        temp += 1
    temp = y
    while temp >= 0:
        sign = grid[x][temp]
        if (sign == "*" or sign == "x"):
            validArray[x][temp] = True
        elif (sign == "#"):
            break
        temp -= 1
    temp = y
    while temp < col:
        sign = grid[x][temp]
        if (sign == "*" or sign == "x"):
            validArray[x][temp] = True
        elif (sign == "#"):
            break
        temp += 1
    path-=1

x,y=findFirstValid(0,0)
while y<col:
    dp(x,y,0)
    y+=1
print(maxmum)