import itertools
t=int(input())
points=[]
for i in range(t):
    points.append(list(map(int,input().split(','))))
EPS = 1e-7
points = set(map(tuple, points))
ans = float('inf')
for p1, p2, p3 in itertools.permutations(points, 3):

    p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
    if p4 in points:
        v21 = [p2[0]-p1[0],p2[1]-p1[1]]
        v31 = [p3[0]-p1[0],p3[1]-p1[1]]
        if v21[0]*v31[0]+v21[1]*v31[1]==0:
            area =( (v21[0]**2+v21[1]**2)**0.5)*( (v31[0]**2+v31[1]**2)**0.5)
            if area < ans:
                ans = area

if ans < float('inf'):
    print("%.4f"%ans)
else:
    print('0.0000')