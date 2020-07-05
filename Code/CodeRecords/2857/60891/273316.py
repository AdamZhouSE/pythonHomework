
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
print(gcd_)

