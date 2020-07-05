class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y   

def cross(p1,p2,p3):
    x1=p2.x-p1.x
    y1=p2.y-p1.y
    x2=p3.x-p1.x
    y2=p3.y-p1.y
    return x1*y2-x2*y1     

def IsIntersec(p1,p2,p3,p4): 

    if(max(p1.x,p2.x)>=min(p3.x,p4.x)  
    and max(p3.x,p4.x)>=min(p1.x,p2.x)  
    and max(p1.y,p2.y)>=min(p3.y,p4.y)  
    and max(p3.y,p4.y)>=min(p1.y,p2.y)): 

        if(cross(p1,p2,p3)*cross(p1,p2,p4)<=0
           and cross(p3,p4,p1)*cross(p3,p4,p2)<=0):
            D=1
        else:
            D=0
    else:
        D=0
    return D

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    t1 = getInput()
    t2 = getInput()
    
    p1 = point(t1[0], t1[1])
    p2 = point(t1[2], t1[3])
    p3 = point(t2[0], t2[1])
    p4 = point(t2[2], t2[3])
    
    print(IsIntersec(p1,p2,p3,p4))