data = list(map(int, input().split(',')))
target = int(input())
result, distance = 0, target
for i in range(1, max(data)+1):
    tmp = 0
    for j in data:
        if j > i:
            tmp += i
        else:
            tmp += j
    if abs(target - tmp) < distance:
        distance = abs(target - tmp)
        result = i
print(result)
