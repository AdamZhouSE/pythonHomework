# https://blog.csdn.net/s0rose/article/details/78831570

class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

def cross(p1,p2,p3):
    x1 = p2.x - p1.x
    y1 = p2.y - p1.y
    x2 = p3.x - p1.x
    y2 = p3.y - p1.y
    return x1 * y2 - x2 * y1

def quickOut(p1,p2,p3,p4):
    if (max(p1.x, p2.x) >= min(p3.x, p4.x)
    and max(p3.x, p4.x) >= min(p1.x, p2.x)
    and max(p1.y, p2.y) >= min(p3.y, p4.y)
    and max(p3.y, p4.y) >= min(p1.y, p2.y)):
        return True
    return False

def judge(p1,p2,p3,p4):
    if quickOut(p1,p2,p3,p4):
        if (cross(p1, p2, p3) * cross(p1, p2, p4) <= 0 and cross(p3, p4, p1) * cross(p3, p4, p2) <= 0):
            res = 1
        else:
            res = 0
    else:
        res = 0
    return res

def solve():
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=map(int,input().split())
    p1=point(x1,y1)
    p2=point(x2,y2)
    p3=point(x3,y3)
    p4=point(x4,y4)
    
    print(judge(p1,p2,p3,p4))
    
if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()
