str = input()
n = int(str)
ans = n - 1


def gcd(a, b):
    if (b == 0):
        return a
    if (b == 1):
        return a-1
    return gcd(b, a % b) + a // b


for i in range(1, n):
    ans = min(gcd(n, i), ans)

print(ans,end="")
