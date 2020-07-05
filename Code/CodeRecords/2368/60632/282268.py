t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    tmp = []
    for j in range(n):
        if j % 2 == 0:
            tmp.append(max(data[0], data[-1]))
            data.remove(tmp[-1])
        else:
            tmp.append(min(data[0], data[-1]))
            data.remove(tmp[-1])
    result.append(tmp)
for i in result:
        print(*i,end=' ')
        print()
