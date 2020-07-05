t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    tmp = [-1]
    for j in range(1, n):
        if min(data[:j]) >= data[j]:
            nearest = -1
        else:
            nearest = [x for x in data[:j] if x < data[j]][-1]
        tmp.append(nearest)
    result.append(tmp)
for i in result:
    print(*i,end=' ')
    print()
