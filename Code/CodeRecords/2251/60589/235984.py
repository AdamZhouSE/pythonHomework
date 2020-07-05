def area(p, q, r):
    return .5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                    - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])


num=int(input())
points=[]
areas=[]
for i in range(num):
    point=input().split(',')
    point=list(map(int,point))
    points.append(point)
for i in range(num):
    for j in range(i+1,num):
        for k in range(j+1,num):
            areas.append(area(points[i],points[j],points[k]))
print(max(areas))