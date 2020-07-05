dic = {} #表示朝向
dic[1] = "N"
dic[2] = "E"
dic[3] = "S"
dic[4] = "W"

def changePosition(x, y, order, step, orientation):
    if order == "U":
        if orientation == 1:
            y+=step
            return x,y,orientation
        if orientation == 2:
            x+=step
            return x,y,orientation
        if orientation == 3:
            y-=step
            return x,y,orientation
        if orientation == 4:
            x-=step
            return x,y,orientation
    if order == "D":
        if orientation == 1:
            orientation = 3
            y-=step
            return x,y,orientation
        if orientation == 2:
            orientation = 4
            x-=step
            return x,y,orientation
        if orientation == 3:
            orientation = 1
            y+=step
            return x,y,orientation
        if orientation == 4:
            orientation = 2
            x+=step
            return x,y,orientation
    if order == "L":
        if orientation == 1:
            orientation = 4
            x-=step
            return x,y,orientation
        if orientation == 2:
            orientation = 1
            y+=step
            return x,y,orientation
        if orientation == 3:
            orientation = 2
            x+=step
            return x,y,orientation
        if orientation == 4:
            orientation = 3
            y-=step
            return x,y,orientation
    if order == "R":
        if orientation == 1:
            orientation = 2
            x+=step
            return x,y,orientation
        if orientation == 2:
            orientation = 3
            y-=step
            return x,y,orientation
        if orientation == 3:
            orientation = 4
            x-=step
            return x,y,orientation
        if orientation == 4:
            orientation = 1
            y+=step
            return x,y,orientation


t  = int(input())
for _ in range(t):
    s = input()
    x,y = 0,0
    orientation = 1
    orders = input().split(" ")
    for i in range(0,len(orders),2):
        x,y,orientation = changePosition(x,y,orders[i],int(orders[i+1]),orientation)
    print(int(pow(pow(x,2)+pow(y,2),0.5)),dic[orientation])
