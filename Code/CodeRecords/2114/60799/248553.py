def solve(n) -> int:
    while n % 4 == 0:
        n = int(n / 4)
    if n % 8 == 7:
        return 4
    for a in range(int(n ** 0.5)):
        b = int((n - a * a) ** 0.5)
        if (a * a + b * b) == n:
            if a == 0:
                return 1
            else:
                return 2
    return 3


print(solve(int(input())))
