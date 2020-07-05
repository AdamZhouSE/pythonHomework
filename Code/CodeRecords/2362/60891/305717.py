n = int(input())
ans = 0
if n == 1:
    ans = 1
elif n == 2:
    ans = 2
elif n == 3:
    ans = 3
elif n == 4:
    ans = 7
elif n > 4:
    ans = n * (n - 1) // (n - 2) + (n - 3)
    n -= 4
    while n >= 4:
        ans -= n * (n - 1) // (n - 2)
        ans += n - 3
        n -= 4
    if n == 1:
        ans -= 1
    elif n == 2:
        ans -= 2
    elif n == 3:
        ans -= 3
    else:
        ans = ans
else:
    ans = 0
print(ans)
