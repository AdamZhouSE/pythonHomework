n = int(input())

ans = 1

if n == 1 or n == 2:
    ans = 1
elif n == 3:
    ans = 2
else:
    while n > 4:
        ans *= 3
        n -= 3
    ans*=n

print(ans)
