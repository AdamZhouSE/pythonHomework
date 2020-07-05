t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    total = 0
    for j in range(0, n - 1):
        total += data[j + 1:].count(data[j])
    result.append(total)
for i in result:
    print(i)
