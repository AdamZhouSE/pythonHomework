"""
回旋镖定义为一组三个点，这些点各不相同且不在一条直线上
给出平面上三个点组成的列表，判断这些点是否可以构成回旋镖
"""

n=int(input())
coordinates=[]

for i in range(n):
    coordinates.append([int(m) for m in str(input()).split(",")])

if (coordinates[2][1]-coordinates[0][1])/(coordinates[2][0]-coordinates[0][0])!=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0]):
        print("True")
else:
    print("False")