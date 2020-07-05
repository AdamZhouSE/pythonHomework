#01
R = int(input())
C = int(input())
r0 = int(input())
c0 = int(input())

matrix = []
pointAndDistance = {}
outcome = []
for i in range(0,R): # 初始化
    for j in range(0,C):
        part = [i,j]
        matrix.append(part)

for i in range(0,len(matrix)):
    distance = abs(matrix[i][0]-r0) + abs(matrix[i][1]-c0)
    pointAndDistance[i] = distance

Distance = sorted(pointAndDistance.values())

# for item in pointAndDistance.keys():
#     outcome.append(matrix[item])
for d in Distance:
    for item in pointAndDistance.keys():
        if pointAndDistance[item] == d:
            outcome.append(matrix[item])
            pointAndDistance[item] = -1
            break

print(outcome)