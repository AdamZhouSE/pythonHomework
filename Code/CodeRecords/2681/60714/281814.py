T = int(input())
for i in range(0, T):
    n = int(input())
    ans = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
            ans += 1
        else:
            n = n - 1
            ans += 1
    print(ans)
