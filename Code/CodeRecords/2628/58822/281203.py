def IsTrangleOrArea(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def IsInside(x1, y1, x2, y2, x3, y3, x, y):
    if(x==x1 and y==y1):
        return 0
    if (x == x2 and y == y2):
        return 0
    if (x == x3 and y == y3):
        return 0
    if(x1==x2):
        k1=10000
        if(x==x1):
            return 0
    else:
        k1 = (y1 - y2) / (x1 - x2)
    if(x2==x3):
        k3=10001
        if(x==x2):
            return 0
    else:
        k3 = (y3 - y2) / (x3 - x2)
    if(x1==x3):
        k2=10002
        if(x==x1):
            return 0
    else:
        k2 = (y1 - y3) / (x1 - x3)
    '''k1=(y1-y2)/(x1-x2)
    k2=(y1-y3)/(x1-x3)
    k3=(y3-y2)/(x3-x2)'''
    if(x==x1):
        kk1=10003
    else:
        kk1=(y-y1)/(x-x1)
    if(x==x2):
        kk2=10004
    else:
        kk2 = (y - y2) / (x - x2)
    if(x==x3):
        kk3=10005
    else:
        kk3 = (y - y3) / (x - x3)
    if(kk1==k1 or kk1==k2 or  kk1==k3 ):
        return 0
    if (kk2 == k1 or kk2 == k2 or kk2 == k3):
        return 0
    if (kk3 == k1 or kk3 == k2 or kk3 == k3):
        return 0
    # 三角形ABC的面积
    ABC = IsTrangleOrArea(x1, y1, x2, y2, x3, y3)
    # 三角形PBC的面积
    PBC = IsTrangleOrArea(x, y, x2, y2, x3, y3)
    # 三角形ABC的面积
    PAC = IsTrangleOrArea(x1, y1, x, y, x3, y3)
    # 三角形ABC的面积
    PAB = IsTrangleOrArea(x1, y1, x2, y2, x, y)
    if(ABC == PBC + PAC + PAB):
        return 1
    else:
        return 0

def cal(a):
    x1=int(a[0])
    y1=int(a[1])
    x2=int(a[2])
    y2=int(a[3])
    x3 = int(a[4])
    y3 = int(a[5])
    ma1=max(x1,x2,x3)
    mi1=min(x1,x3,x3)
    ma2=max(y1,y2,y3)
    mi2=min(y1,y2,y3)
    num=0
    for i in range(mi1,ma1+1):#x
        for k in range(mi2,ma2+1):#y
            if(IsInside(x1, y1, x2, y2, x3, y3, i,k)==1):
                num+=1
    return num
n=input()
li=[]
for i in range(0,int(n)):
    li1=[]
    li1=input().split(' ')
    li1.extend(input().split(' '))
    li1.extend(input().split(' '))
    li.append(li1)
for i in range(int(n)):
    print(cal(li[i]))