import itertools
n=int(input())
points=[]
for i in range(n):
    points.append(list(map(int,input().split(","))))
res=float('inf')
for p1,p2,p3 in itertools.permutations(points,3):
    p4=[p2[0]+p3[0]-p1[0],p2[1]+p3[1]-p1[1]]
    if p4 in points:
        v1=complex(p2[0]-p1[0],p2[1]-p1[1])
        v2=complex(p3[0]-p1[0],p3[1]-p1[1])
        if abs(v1.real*v2.real+v1.imag*v2.imag)<1e-7:
            res=min(res,abs(v1)*abs(v2))
if res==float('inf'):
    print('0.0000')
else:
    print("{:.4f}".format(res))
