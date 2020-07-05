n = int(input())
for i in range(0, n):
    ans = 1
    p, q = [int(x) - 1 for x in input().split()]
    for j in range(max(p, q) + 1, p + q + 1):
        ans *= j
    for j in range(1, min(p, q) + 1):
        ans = ans // j
    print(ans)

