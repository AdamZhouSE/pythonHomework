
def gcd(a, b):
    # a作为除数 必须大于b
    a, b = (a, b) if a >= b else (b, a)
    while b:
        a, b = b, a % b
    return a


def isPrime(k):
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True


n = int(input())
a = [int(i) for i in input().split()]
if n == 1:
    gcd_ = a[0]
else:
    gcd_ = gcd(a[0], a[1])
    for i in range(2, n):
        gcd_ = gcd(gcd_, a[i])
x = gcd_
ans = 1
i = 2
while i <= x and i * i <= x:
    if isPrime(i):
        cnt = 0
        while x % i == 0:
            x //= i
            cnt += 1
        ans *= (cnt + 1)
    i += 1
if x > 1:
    ans *= 2

print(ans)
