def gcd(a, b):
    if b == 0:
        return -1
    if b == 1:
        return a - 1
    nextgcd = gcd(b, a % b)
    if nextgcd != -1:
        return nextgcd + a // b
    return -1


n = int(input())
res = 0
for i in range(1, (n + 1) // 2 + 1):
    cnt = gcd(n, i)
    if cnt != -1:
        if res == 0:
            res = cnt
        else:
            res = min(res, cnt)
print(res, end = "")
