n, p = map(int, input().split(' '))
data = list(map(int, input().split(' ')))
m = int(input())
operations = []
for i in range(m):
    operations.append(list(map(int, input().split(' '))))
result = []
for i in operations:
    if i[0] == 1:
        t, g, c = i[1], i[2], i[3]
        for j in range(t - 1, g):
            data[j] *= c
    elif i[0] == 2:
        t, g, c = i[1], i[2], i[3]
        for j in range(t - 1, g):
            data[j] += c
    elif i[0] == 3:
        t, g = i[1], i[2]
        tmp = sum(data[t - 1:g])
        result.append(tmp % p)
for i in result:
    print(i)
