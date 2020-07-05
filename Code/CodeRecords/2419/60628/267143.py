def differenceOfProductAndSum(n):
    s = 0
    prod = 1
    while (n > 0):
        r = n % 10
        n //= 10
        prod *= r
        s += r
    return prod - s

n = int(input())
print(differenceOfProductAndSum(n))