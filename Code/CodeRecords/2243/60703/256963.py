p = int(input())
q = int(input())
def mirror(p,q):
    if(p%q==0):#特殊情况
        if( (p/q)%2==0):
            return 2
        else:return 1
    direction = 1#方向，1代表向上，-1代表向下
    x,y = 0,0
    while (not (x==0 and y==p))  and (not (x==p and y==p)) and (not (x==p and y==0)):
        if(x==0):
            x = p
        else:
            x = 0
        if(direction==1):
            y+=q
            if(y>p):
                y = p-(y-p)
                direction = -1
        else:
            y-=q
            if(y<0):
                y = 0+(0-y)
                direction = 1


    if(x==0 and y==p):
        return 2
    elif x==p and y==p:
        return 1
    return 0

print(mirror(p,q))

