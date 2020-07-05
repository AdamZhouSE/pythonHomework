def b(n):
    if n == 1: return 1
    r = 0
    for i in range(2, n // 2):
        r = max(r, i * (n - i), i * b(n - i))
print(b(int(input())))