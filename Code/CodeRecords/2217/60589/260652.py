points=[]
for i in range(4):
    point=input().split(',')
    point=list(map(int,point))
    points.append(point)
distance=set()
for i in range(len(points)):
    for j in range(i+1,len(points)):
        p_1=points[i]
        p_2=points[j]
        dis=(p_1[0]-p_2[0])**2+(p_1[1]-p_2[1])**2
        distance.add(dis)
print(True if len(distance)==2 else False)