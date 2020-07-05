def divisor(n: int):
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):
            return i


def prime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def add(n: int):
    return n if n < 10 else sum(list(map(int, list(str(n)))))


def func32():
    for time in range(0, eval(input())):
        n: int = int(input())
        res = 0
        tem = n if prime(n) else add(n)
        while not prime(n):
            t = divisor(n)
            res += add(t)
            n //= t
        if tem == res + add(n):
            print(1)
        else:
            print(0)
    

func32()
