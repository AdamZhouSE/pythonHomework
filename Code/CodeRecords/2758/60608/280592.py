
def binom(n: int, m: int, arr1: list, arr2: list, p: int):
    return 0 if m > n else arr1[n] * arr2[m] % p * arr2[n - m] % p


def lucas(n: int, m: int, arr1: list, arr2: list, p: int):
    if m > n:
        return 0
    return 1 if m == 0 else binom(n % p, m % p, arr1, arr2, p) * lucas(n // p, m // p, arr1, arr2, p) % p


def func5():
    arr = list(map(int, input().split()))
    n, m, res, arr1, arr2, p = arr[0], arr[1], [1, 1], [1], [1], 10007
    for i in range(2, p):
        res.append(-(p // i) * res[p % i] % p + p)
    for i in range(1, p):
        arr1.append(arr1[i - 1] * i % p)
        arr2.append(arr2[i - 1] * res[i] % p)
    print(lucas(n * m, n - 1, arr1, arr2, p) * res[n] % p)


func5()
