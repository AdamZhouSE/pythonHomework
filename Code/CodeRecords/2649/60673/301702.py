t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    n = int(inp[0])
    L = int(inp[1])
    R = int(inp[2])
    bina = []
    while True:
        s = n // 2
        y = n % 2
        bina.append(y)
        if s == 0:
            break
        n = s
    res = 0
    length = len(bina)
    for i in range(0, length):
        if (L - 1) <= i <= (R - 1):
            if bina[i] == 0:
                res += pow(2, i)
            if bina[i] == 1:
                continue
        else:
            res += bina[i] * pow(2, i)
    print(res)