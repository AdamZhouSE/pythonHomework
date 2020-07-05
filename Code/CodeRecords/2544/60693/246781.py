def mult(p1:list,p2:list,p3:list):
    # return p1p2 x p1p3
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

def is_intersect(p1:list,p2:list,q1:list,q2:list):
    if max(p1[0],p2[0])<min(q1[0],q2[0]) or max(q1[0],q2[0])<min(p1[0],p2[0]):
        return False
    if max(p1[1],p2[1])<min(q1[1],q2[1]) or max(q1[1],q2[1])<min(p1[1],p2[1]):
        return False
    if mult(p1,p2,q1)*mult(p1,p2,q2)>0:return False
    if mult(q1,q2,p1)*mult(q1,q2,p2)>0:return False
    return True

cases=int(input())
for i in range(cases):
    line1=list(map(int,input().split()))
    line2=list(map(int,input().split()))
    x1,y1,x2,y2=line1[0],line1[1],line1[2],line1[3]
    x3,y3,x4,y4=line2[0],line2[1],line2[2],line2[3]
    if is_intersect([x1,y1],[x2,y2],[x3,y3],[x4,y4]):print(1)
    else:print(0)
