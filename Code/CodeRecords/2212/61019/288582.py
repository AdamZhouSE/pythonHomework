t = int(input())
for _ in range(t):
    n = int(input())
    total = 0
    for i in range(1, round(pow(n, 0.5)) + 1):
        if n % i == 0:
            total += i
            total += n // i
    print(1) if total < 2 * n else print(0)
