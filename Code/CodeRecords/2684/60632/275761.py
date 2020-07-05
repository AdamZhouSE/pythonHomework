t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    res, tmp = 0, []
    for j in range(0, len(data), 2):
        res += data[j]
    tmp.append(res)
    res = 0
    for j in range(1, len(data), 2):
        res += data[j]
    tmp.append(res)
    res = 0
    for j in range(0, len(data), 3):
        if j <= len(data) - 3:
            res += data[j + 1] + data[j + 2]
        else:
            res += sum(data[j:]) - data[j]
    tmp.append(res)
    result.append(min(tmp))
for i in result:
    print(i)
