"""
在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标
其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点
请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false
"""

n=int(input())
coordinates=[]

for i in range(n):
    coordinates.append([int(m) for m in str(input()).split(",")])

slope=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])

result=True
i=2
while i<n:
    if (coordinates[i][1]-coordinates[0][1])/(coordinates[i][0]-coordinates[0][0])!=slope:
        result=False
    i+=1

if result:
    print("True")
else:
    print("False")