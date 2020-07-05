n = int(input())
m = 1
while m * m <= n:
    m += 1
m -= 1
ans = 0
while n > 0:
    while m * m <= n:
        n -= m * m
        ans += 1
    m -= 1
print(ans)