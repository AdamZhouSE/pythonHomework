T = int(input())
for i in range(T):
    n = int(input())
    ans = 0
    while n != 0:
        if n % 2 == 1:
            n -= 1
        else:
            n //= 2
        ans += 1
    print(ans)