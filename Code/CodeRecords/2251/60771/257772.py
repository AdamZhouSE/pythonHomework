#01
n = int(input())
points = []
for i in range(0,n):
    ori = input().split(",")
    num = [float(item) for item in ori]
    points.append(num)
# print(points)
points.sort()
# print(points)
start = points[0]
index = 0
for i in range(0,n):
    if start[0] == points[i][0]:
        continue
    else:
        index = i-1
        break
length = points[index][1] - start[1]
# print(length)
width = points[n-1][0] - start[0]
# print(width)
s = abs(length*width / 2)
print(s)