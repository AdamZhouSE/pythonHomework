def euclid(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    dis=((x2-x1)**2+(y2-y1)**2)**0.5
    return dis

def manhattan(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    dis=abs(x2-x1)+abs(y2-y1)
    return dis

def findCouples(pts):
    cnt=0
    for i in range(len(pts)-1):
        for j in range(i+1,len(pts)):
            p1=pts[i]
            p2=pts[j]
            if manhattan(p1,p2)==euclid(p1,p2):
                cnt+=1
    return cnt

if __name__=="__main__":
    points=[]
    n=int(input())
    for _ in range(n):
        p=input().split()
        p=[int(x) for x in p]
        points.append(p)
    ans=findCouples(points)
    print(ans)