def isInTrian(x:list,p:list,q:list,r:list,signTrian):
    signPQ=(q[0]-p[0])*(x[1]-p[1])-(q[1]-p[1])*(x[0]-p[0])
    signRP = (p[0]-r[0])*(x[1]-r[1])-(p[1]-r[1])*(x[0]-r[0])
    signQR=(r[0] - q[0]) * (x[1] - r[1]) - (r[1] - q[1]) * (x[0] - r[0])

    d1=(signPQ*signTrian>0)
    d2=(signRP*signTrian>0)
    d3=(signQR*signTrian>0)
    return d1 and d2 and d3


def findPoints(p:list,q:list,r:list):
    res=0
    signTrian=(q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
    left=min(p[0],q[0],r[0])
    right=max(p[0],q[0],r[0])
    down=min(p[1],q[1],r[1])
    up=max(p[1],q[1],r[1])
    for i in range(left,right+1):
        for j in range(down,up+1):
            if isInTrian([i,j],p,q,r,signTrian):
                res+=1
    return res


cases=int(input())
for _ in range(cases):
    p=list(map(int,input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    print(findPoints(p,q,r))