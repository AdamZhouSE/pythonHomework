t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    m = int(inp[0])
    n = int(inp[1])
    a = int(inp[2])
    b = int(inp[3])
    res = []
    for i in range(m, n + 1):
        if i % a == 0:
            if (i in res):
                continue
            else:
                res.append(i)
    for j in range(m, n + 1):
        if j % b == 0:
            if (j in res):
                continue
            else:
                res.append(j)
    print(len(res))