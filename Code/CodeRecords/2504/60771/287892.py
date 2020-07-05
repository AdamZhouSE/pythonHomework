#05
points = eval(input())
K = int(input())

pointsAndDistance = {}
distance = []
res = []

for i in range(0,len(points)):
    d = (points[i][0]-0)*(points[i][0]-0) + (points[i][1]-0)*(points[i][1]-0)
    pointsAndDistance[i] = d
    distance.append(d)

distance.sort()

for d in distance:
    for item in pointsAndDistance.keys():
        if pointsAndDistance[item] == d:
            res.append(points[item])
            pointsAndDistance[item] = -1
            break

print(res[0:K])

