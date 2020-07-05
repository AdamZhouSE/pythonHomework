t = int(input())
for i in range(t):
    a, b, m = map(int, input().split(" "))
    res = 0
    x = 0
    for _ in range(a, b + 1):
        if _ % m == 0:
            x = _
            break
    if x == 0:
        print(0)
        continue
    for j in range(x, b + 1, m):
        res += 1
    print(res)
