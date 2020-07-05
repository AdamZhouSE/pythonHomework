n = int(input())
for i in range(0, n):
    m = int(input())
    block = [int(x) for x in input().split()]
    if block[0] < block[-1]:
        base = block[0]
        ans = 0
        for j in range(0, m):
            if base >= block[j]:
                ans = ans + base - block[j]
            else:
                base = block[j]
    else:
        base = block[-1]
        ans = 0
        for j in range(m - 1, -1, -1):
            if base >= block[j]:
                ans = ans + base - block[j]
            else:
                base = block[j]
    print(ans)
