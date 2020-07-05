import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
begin = 1


def inNumsFn(num):
    return num // a + num // b + num // c - num // math.gcd(a, b) - num // math.gcd(b, c) - num // math.gcd(a,
                                                                                                            c) + num // (
               math.gcd(math.gcd(a, b), c))


if n > 100:
    right = n * min(a, b, c)
    left = n
    mid = 0
    while left < right:
        mid = (left + right) // 2
        if inNumsFn(mid)<n:
            left=mid+1
        else:
            right=mid
    begin=right+1
else:
    while n != 0:
        if begin % a == 0 or begin % b == 0 or begin % c == 0:
            n = n - 1
        begin += 1
print(begin - 1)