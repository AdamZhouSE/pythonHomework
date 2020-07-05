n = int(input())
ans = 0
if n == 0:
    ans = 1
elif n == 1:
    ans = 10
elif n <= 10:
    ans = 10
    f = 9
    for i in range(2, n + 1):
        f *= 11 - i
        ans += f
else:
    ans = 8877691

print(ans)