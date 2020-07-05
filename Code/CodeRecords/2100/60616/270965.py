def trailingZeroes(n):
    if n == 0:
        return 0

    def iter(n):
        if n == 1:
            return 1
        if n >= 2:
            return n * iter(n - 1)

    res = iter(n)
    count = 0
    for i in range(len(str(res))):
        if res % 10 == 0:
            count += 1
            res = res / 10
    return count
num=int(input())
print(trailingZeroes(num))