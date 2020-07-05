def count(n):
    if n == 0 or n == 1:
        return 1
    sum = 0
    for i in range(n):
        sum += count(i)*count(n-1-i)
    return sum


n = int(input())
print(count(n))