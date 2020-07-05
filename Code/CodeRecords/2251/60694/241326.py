# S=(1/2) * abs(x1y2 + x2y3 + x3y1 - x1y3 - x2y1 - x3y2)
n = int(input())
points = []
for i in range(n):
    point = []
    x, y = map(int, input().split(","))