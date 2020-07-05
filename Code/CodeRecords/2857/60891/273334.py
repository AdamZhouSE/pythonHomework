
def gcd(a, b):
    # a作为除数 必须大于b
    a, b = (a, b) if a >= b else (b, a)
    while b:
        a, b = b, a % b
    return a


def isPrime(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


n = int(input())
a = [int(i) for i in input().split()]
gcd_ = gcd(a[0], a[1])
for i in range(2, n):
    gcd_ = gcd(gcd_, a[i])
x = gcd_
ans = 1
tmp = []
for i in range(2,gcd+1):
    if isPrime(i):
        tmp.append(i)
for i in tmp:
    if isPrime(i):
        cnt = 0
        while x % i == 0:
            x //= i
            cnt += 1
        ans *= (cnt + 1)
    if x == 1:
        break
print(ans)
