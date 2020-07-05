T = int(input())
for _ in range(T):
    n = int(input())
    res = []
    while n > 0:
        res.append(n%2)
        n //= 2
    a = len(res) - sum(res)
    b = sum(res)
    print(a ^ b)

