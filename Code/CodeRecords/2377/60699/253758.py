n=int(input())
points=[]
for i in range(n):
    points.append(list(map(int,input().split(','))))
if points[0][0]==points[1][0] and points[0][1]==points[1][1] or points[0][0]==points[2][0] and points[0][1]==points[2][1] or points[2][0]==points[1][0] and points[1][0]==points[2][0]:
    print(False)
else:
    if (points[2][0]-points[0][0])*(points[1][1]-points[0][1])==(points[2][1]-points[0][1])*(points[1][0]-points[0][0]):
        print(False)
    else:
        print(True)