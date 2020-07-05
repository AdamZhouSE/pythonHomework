t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    a = int(inp[0])
    b = int(inp[1])
    c = int(inp[2])
    res = 1
    t = a % c
    while b:
        if b & 1:
            res = res * t % c
        t = t * t % c
        b >>= 1
    print(res)