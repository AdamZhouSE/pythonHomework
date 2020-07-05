data = list(map(int, input().split(',')))
target = int(input())
result = target
for i in range(min(data), max(data)+1):
    tmp = 0
    for j in data:
        if j > i:
            tmp += i
        else:
            tmp += j
    distance = abs(target - tmp)
    if distance < result:
        result = distance
print(result)
