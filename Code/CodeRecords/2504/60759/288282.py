from math import sqrt


points = eval(input())
k = int(input())
dis = []
ans = []
for point in points:
    dis.append([point, sqrt(pow(point[0], 2) + pow(point[1], 2))])
dis = sorted(dis, key=lambda item: item[1])
for i in range(k):
    ans.append(list(dis[i][0]))
print(ans)
