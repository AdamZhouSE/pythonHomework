def checkline(x1,y1,x2,y2,x3,y3,x4,y4):
    if((y2-y1)/(x2-x1)==(y3-y4)/(x3-x4)):
        return "0"
    if(x1==x2):
        if(x3!=x4):
            y=(y3-y4)*(x1-x3)/(x3-x4)
            s=[y1,y2].sort()
            if(y>s[0] and y<s[1]):
                return "1"
            else:
                return "0"
        else:
            return "0"
    elif(x3==x4):
        return checkline(x3,y3,x4,y4,x1,y1,x2,y2)
    x=(y3-y2-x3*(y3-y4)/(x3-x4)+x2*(y2-y1)/(x2-x1))/((y2-y1)/(x2-x1)-(y3-y4)/(x3-x4))
    if(x1<x2):
        if(x<x1 or x>x2):
            return "0"
        elif(x3<x4):
            if(x<x3 or x>x4):
                return "0"
            else:
                return "1"
    else:
        if(x<x2 or x>x1):
            return "0"
        elif(x3<x4):
            if(x<x3 or x>x4):
                return "0"
            else:
                return "1"
n=int(input())
for i in range(n):
    x1,y1,x2,y2=map(int,input().split(" "))
    x3,y3,x4,y4=map(int,input().split(" "))
    print(checkline(x1,y1,x2,y2,x3,y3,x4,y4))
    
            