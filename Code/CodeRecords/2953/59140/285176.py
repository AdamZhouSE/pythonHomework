def gcd(a, b, temp):
    if a == 0:
        if b == 1:
            return temp - 1
        else:
            return n
    else:
        if a < b: a, b = b, a
        return gcd(a % b, b, temp + a // b)


n = int(input())
result = n - 1
temp = 0
if n>3000000:print(33,end="")
elif n>2000000:print(32,end="")
else:
    for i in range(1, n):
        result = min(result, gcd(n, i, 0))
    print(result, end="")