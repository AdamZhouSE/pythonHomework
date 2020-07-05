n = int(input())
if n > 10:
    n = 10
def fac(n):
    if n <= 1: return 1
    else: return n * fac(n - 1)
ans = 10
for i in range(2, n + 1):
    ans += 9 * fac(9) // fac(10 - i)
print(ans)