T = int(input())
for _ in range(T):
    n = int(input())
    res = []
    while n > 0:
        res.append(n%2)
        n //= 2
    if sum(res) % 2 == 0:
        print("even")
    else:
        print("odd")

