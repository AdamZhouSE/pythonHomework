n=int(input())
points={}
for i in range(n):
    points[i]=sum(map(int,input().split()))
rank=sorted(points.values(),reverse=True)
print(rank.index(points[0])+1)