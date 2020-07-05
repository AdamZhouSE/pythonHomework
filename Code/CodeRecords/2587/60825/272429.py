def minTimeToVisitAllPoints(points):
    x0, x1 = points[0]
    ans = 0
    for i in range(1, len(points)):
        y0, y1 = points[i]
        ans += max(abs(x0 - y0), abs(x1 - y1))
        x0, x1 = points[i]
    return ans

N=int(input())
ins=[]
for i in range(N):
    s=input()
    l=s.split(',')
    l= list(map(int, l))
    ins.append([l[0], l[1]])
print(minTimeToVisitAllPoints(ins))