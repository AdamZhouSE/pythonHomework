def f(n):
    if n == 1: return 1
    return n * f(n - 1)
n = int(input())
print(f(2 * n) // f(n) // f(n) // (n + 1) % 1000000007)