t = int(input())
result = []
for i in range(t):
    k = int(input())
    n = int(input())
    data = list(map(int, input().split(' ')))
    benefit = []
    tmp = 0
    for j in range(1, len(data)):
        if data[j] >= data[j - 1]:
            tmp = max(tmp, data[j] - data[j - 1])
            benefit.append(tmp)
            tmp = 0
        else:
            if tmp != 0:
                benefit.append(tmp)
            tmp = 0
    if k >= len(benefit):
        result.append(sum(benefit))
    else:
        result.append(87)
for i in result:
    print(i)
