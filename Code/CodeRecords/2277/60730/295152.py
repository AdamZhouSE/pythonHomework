def recursive(k, n):
    if n == 0 or n == 1 or k == 1:
        return n
    min = n
    for i in range(1, n + 1):
        tmin = max(recursive(k - 1, i - 1), recursive(k, n - i))
        min = min(min, 1 + tmin)
    return min


k = int(input())
n = int(input())
print(recursive(k, n))
