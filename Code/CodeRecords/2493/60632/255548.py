m, n = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
areas = []
result = []
for i in range(n):
    areas.append(list(map(int, input().split(' '))))
for i in areas:
    result.append(len(list(set(data[i[0]-1:i[1]]))))
print(*result)
