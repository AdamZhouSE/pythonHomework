def integerBreak( n):
    if n <= 3: return n - 1
    a, b = n // 3, n % 3
    if b == 0: return pow(3, a)
    if b == 1: return pow(3, a - 1) * 4
    return pow(3, a) * 2

n = int(input())
print(integerBreak(n))