def count_different(n):
    if n > 10:
        return count_different(10)
    if n == 1:
        return 10
    current = 9
    for i in range(n-1):
        current *= 9 - i
    return count_different(n-1) + current

n = int(input())
result = count_different(n)
print(result)