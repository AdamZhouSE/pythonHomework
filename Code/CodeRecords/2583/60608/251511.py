def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


def lcd2(a: int, b: int):
    return a * b // gcd(a, b)


def lcd3(a: int, b: int, c: int):
    return a * lcd2(b, c) // gcd(a, lcd2(b, c))


def uglyNum(n: int, a: int, b: int, c: int):
    return n // a + n // b + n // c - n // lcd2(a, b) - n // lcd2(b, c) - n // lcd2(a, c) + n // lcd3(a, b, c)



def func27():
    n = eval(input())
    a = eval(input())
    b = eval(input())
    c = eval(input())
    left = 1
    right = n * min(a, b, c)
    while left < right:
        mid = (left + right) // 2
        t = uglyNum(mid, a, b, c)
        if t < n:
            left = mid + 1
        else:
            right = mid
    print(left)

func27()