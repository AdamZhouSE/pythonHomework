def manhd(points):
    return abs(points[1][0] - points[0][0]) + abs(points[1][1] - points[0][1])


def oD(points):
    return pow(pow(points[1][0] - points[0][0], 2) + pow(points[1][1] - points[0][1], 2), 0.5)


t = int(input())
n = int(input())
ans = []
for i in range(t):
    point = []
    res = 0
    for j in range(n):
        a,b = map(int ,input().split())
        point.append([a,b])
    for j in range(0,n-1):
        for k in range(j+1,n):
            tpoint = [point[j],point[k]]
            if manhd(tpoint)==oD(tpoint):
                res = res+1
    ans.append(res)
for i in ans:
    print(i)