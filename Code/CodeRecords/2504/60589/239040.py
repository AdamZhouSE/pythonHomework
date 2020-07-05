points=input()
K=int(input())
points= points[1:-1].split('],[')
points[0]= points[0][1:]
points[len(points) - 1]= points[len(points) - 1][:-1]
for i in range(len(points)):
    points[i]=points[i].split(',')
    points[i]=list(map(int, points[i]))
points=sorted(points,key=lambda p:p[0]**2+p[1]**2)
print(points[:K])