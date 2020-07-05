class point(): #定义类
    def __init__(self,x,y):
        self.x=x
        self.y=y   

    def cross(p1,p2,p3):#跨立实验
        x1=p2.x-p1.x
        y1=p2.y-p1.y
        x2=p3.x-p1.x
        y2=p3.y-p1.y
        return x1*y2-x2*y1     

    def IsIntersec(p1,p2,p3,p4): #判断两线段是否相交

    #快速排斥，以l1、l2为对角线的矩形必相交，否则两线段不相交
        if(max(p1.x,p2.x)>=min(p3.x,p4.x)    #矩形1最右端大于矩形2最左端
        and max(p3.x,p4.x)>=min(p1.x,p2.x)   #矩形2最右端大于矩形最左端
        and max(p1.y,p2.y)>=min(p3.y,p4.y)   #矩形1最高端大于矩形最低端
        and max(p3.y,p4.y)>=min(p1.y,p2.y)): #矩形2最高端大于矩形最低端

    #若通过快速排斥则进行跨立实验
            if(cross(p1,p2,p3)*cross(p1,p2,p4)<=0
               and cross(p3,p4,p1)*cross(p3,p4,p2)<=0):
                D=1
            else:
                D=0
        else:
            D=0
        return D



import numpy
import math
t=int(input())
for i in range(t):
    a1=input().split()
    a2=input().split()
    x1=int(a1[0])
    y1=int(a1[1])
    a=[]
    a.append(x1)
    a.append(y1)
    b=[]
    c=[]
    d=[]
    x2=int(a1[2])
    y2=int(a1[3])
    x3=int(a2[0])
    y3=int(a2[1])
    x4=int(a2[2])
    y4=int(a2[3])
    b.append(x2)
    b.append(y2)
    c.append(x3)
    c.append(y3)
    d.append(x4)
    d.append(y4)
    m=point()
    res=m.IsIntersec(a,b,c,d)
    print(res)