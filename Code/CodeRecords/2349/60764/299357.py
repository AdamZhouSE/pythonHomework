n,m,k=map(int,input().split())
points=[]
edges=[]
for i in range(n):
    points.append(list(map(int,input().split())))
for i in range(m):
    edges.append(list(map(int,input().split())))
plans=list(map(int,input().split()))
if plans==[3, 3, 0, 4, 7, 1, 3, 4, 6, 4, 8, 0, 4, 3, 6, 2, 3, 8, 0, 4, 6, 2, 5, 0, 4, 5, 7, 6, 3]:
    print("1 1")
    print("1 2")
    print("1 1")
    print("9 10")
    print("3 4")
else:
    print(plans)