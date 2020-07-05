nums=int(input())
def getDis(point1,point2):
    return [point1[0]-point2[0],point1[1]-point2[1]]

def cross_mul(point1,point2):
    return point1[0]*point2[1]-point1[1]*point2[0]
for i in range(nums):
    line1=list(map(int,input().split(" ")))
    line2=list(map(int,input().split(" ")))
    a=line1[0:2]
    b=line1[2:]
    c=line2[0:2]
    d=line2[2:]
    ab=getDis(a,b)
    ac=getDis(a,c)
    ad=getDis(a,d)
    cd=getDis(c,d)
    ca=getDis(c,a)
    cb=getDis(c,b)
    if cross_mul(ab,ac)==0:
        print(1)
    elif cross_mul(ab,ac)*cross_mul(ab,ad)<0 and cross_mul(cd,ca)*cross_mul(cd,cb)<0:
        print(1)
    else:
        print(0)

