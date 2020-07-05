"""
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上
"""

def most_count(arr):
    max=0
    for i in arr:
        if arr.count(i)>max:
            max=arr.count(i)
    return max


n=int(input())
coordinates=[]

for i in range(n):
    coordinates.append([int(m) for m in str(input()).split(",")])

slope_list=[]
for i in range(len(coordinates)):
    slope=[]
    for m in range(len(coordinates)):
        if (coordinates[i][0]!=coordinates[m][0]):
            slope.append((coordinates[i][1]-coordinates[m][1])/(coordinates[i][0]-coordinates[m][0]))
    slope_list.append(most_count(slope)+1)

print(max(slope_list))