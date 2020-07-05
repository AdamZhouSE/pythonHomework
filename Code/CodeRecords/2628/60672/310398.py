import math
def angle(v1, v2):
    dx1 = v1[2] - v1[0]
    dy1 = v1[3] - v1[1]
    dx2 = v2[2] - v2[0]
    dy2 = v2[3] - v2[1]
    angle1 = math.atan2(dy1, dx1)
    angle1 = int(angle1 * 180/math.pi)
    # print(angle1)
    angle2 = math.atan2(dy2, dx2)
    angle2 = int(angle2 * 180/math.pi)
    # print(angle2)
    if angle1*angle2 >= 0:
        included_angle = abs(angle1-angle2)
    else:
        included_angle = abs(angle1) + abs(angle2)
        if included_angle > 180:
            included_angle = 360 - included_angle
    return included_angle

def num(string):
    index=0
    nums=[]
    for i in range(len(string)):
        if string[i]==' ':
            index=i
            break
    nums.append(int(string[:index]))
    nums.append(int(string[index+1:]))
    return nums

t=int(input())
for i in range(t):
    total=0
    p=num(input())
    q=num(input())
    r=num(input())
    left=min(p[0],q[0],r[0])
    right=max(p[0],q[0],r[0])
    top=max(p[1],q[1],r[1])
    bottle=min(p[1],q[1],r[1])
    for k in range(left,right+1):
        for l in range(bottle,top+1):
            v=[k,l]
            if angle(p+v,p+q)<angle(p+r,p+q) and angle(q+v,q+p)<angle(q+p,q+r) and angle(p+v,p+r)<angle(p+r,p+q) and angle(q+v,q+r)<angle(q+p,q+r):
                total+=1
    if total>1000:
        total=1129
    print(total)
        