def f(n):
    if n % 2 == 1:
        return 2 ** (2 ** ((n + 1) // 2 - 1))
    return 2 ** (3 ** (n // 2 - 1))


T = int(input())
for i in range(T):
    print(f(int(input())))
