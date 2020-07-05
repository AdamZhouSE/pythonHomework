def getPermutation(n, k):
    series = [str(i + 1) for i in range(n)]
    res = ''
    cr = factorial(n)
    while n:
        cr //= n
        n -= 1
        temp = (k - 1) // cr
        res += series.pop(temp)
        k -= cr * temp
    return res


def factorial(n):
    if n < 2:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
n=int(input())
k=int(input())
print(getPermutation(n,k))