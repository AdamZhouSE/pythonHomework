input()
points=[]
for i in range(3):
    points.append([int(x) for x in input().split(',')])
if points[1][1]-points[0][1]==0:
    if points[2][1]-points[1][1]==0:
        print(False)
    else:
        print(True)
else:
    if ((points[1][0]-points[0][0])/(points[1][1]-points[0][1]))!=((points[2][0]-points[1][0])/(points[2][1]-points[1][1])):
        print(True)
    else:
        print(False)