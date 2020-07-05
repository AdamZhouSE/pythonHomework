def b(n):
    if n == 1: return 1
    r = 0
    for i in range(1, n // 2 + 1):
        r = max(r, i * (n - i), i * b(n - i))
    return r
print(b(int(input())))