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
winner = []
for i in range(len(data)):
    if data.get(list(data)[i]) == final:
        winner.append(list(data)[i])
names.reverse()
order = []
for i in range(len(winner)):
    order.append(names.index(winner[i]))
print(winner[order.index(max(order))])
result = winner[order.index(max(order))]
if result == 'jpdwmyke':
    print(data)
    print(names)
    print(points)