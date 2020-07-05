def area(p1:list,p2:list,p3:list):
    dx1=p2[0]-p1[0]
    dx2=p3[0]-p1[0]
    dy1=p2[1]-p1[1]
    dy2=p3[1]-p1[1]
    return abs(dx1*dy2-dx2*dy1)/2.0
T=int(input())
points=[]
for _ in range(0,T):
    point=eval("["+input()+"]")
    points.append(point)
res=0
N=len(points)
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            res=max(res,area(points[i],points[j],points[k]))
print(res)