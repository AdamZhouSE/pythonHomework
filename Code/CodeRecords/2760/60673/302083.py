
t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    n = int(inp[0])
    mon = int(inp[1])
    res = 0
    half_n = n // 2
    res = (n - half_n) * mon
    print(res)