t = int(input())
result = []
for i in range(t):
    n = int(input())
    data = list(map(int, input().split(' ')))
    tmp = []
    for j in range(n):
        for k in range(j+1,n):
            if data[k] >= data[j]:
                tmp.append(data[k])
                break
        if len(tmp) != j+1:
            tmp.append(-1)
    result.append(tmp)
for i in result:
    print(*i)
