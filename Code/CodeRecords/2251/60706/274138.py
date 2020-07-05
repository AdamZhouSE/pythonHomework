from itertools import combinations
def largestTriangleArea(points):
        return max([abs((p[0][0] - p[2][0]) * (p[1][1] - p[2][1]) - (p[1][0] -p[2][0]) * (p[0][1] - p[2][1])) for p in combinations(points, 3)]) / 2.0
n=int(input())
points=[]
for i in range(n):
    list1=input().split(',')
    num=[]
    for j in range(len(list1)):
        num.append(int(list1[j]))
    points.append(num)
ans=largestTriangleArea(points)
print(ans)