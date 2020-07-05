n = int(input())
data = {}
names = []
points = []
for i in range(n):
    name, point = input().split(' ')
    data[name] = 0
    names.append(name)
    points.append(int(point))
for i in range(n):
    data[names[i]] += points[i]
final = max(data.values())
# 分数清零，重新计算，找出先到最高分的winner
for i in range(len(data)):
    data[list(data.keys())[i]] = 0
for i in range(n):
    data[names[i]] += points[i]
    if data.get(names[i]) >= final:
        print(names[i])
        break