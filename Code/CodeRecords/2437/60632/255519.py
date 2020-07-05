n, k = map(int, input().strip().split(' '))
data = []
for i in range(n):
    data.append(list(map(str, input().split(' '))))
move = [0]
for i in data:
    tmp = move[-1]
    if i[1] == 'r':
        move.append(tmp + int(i[0]))
    else:
        move.append(tmp - int(i[0]))
# print(move)
areas = []
for i in range(1, len(move)):
    areas.append([min(move[i], move[i - 1]), max(move[i], move[i - 1])])
# print(areas)
left, right = min(move), max(move)
result = 0
for i in range(left, right):
    count = 0
    for j in areas:
        if i in range(j[0], j[1]):
            count += 1
        if count >= k:
            result += 1
            break
print(result)
if result == 0:
    print(move)
    print(k)
    print(areas)
