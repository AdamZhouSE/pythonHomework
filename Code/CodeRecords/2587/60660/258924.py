#Leetcode1266 切比雪夫距离
n=int(input())
points=[]
for i in range(n):
    points.append(eval('[' + input() + ']'))
x0, x1 = points[0]
ans = 0
for i in range(1, len(points)):
    y0, y1 = points[i]
    ans += max(abs(x0 - y0), abs(x1 - y1))
    x0, x1 = points[i]
print(ans)