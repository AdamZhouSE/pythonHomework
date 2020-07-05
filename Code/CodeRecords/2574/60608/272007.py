def isprime(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def fetch(n: int):
    ans, t, num = 2, 2, 1
    while num < n:
        t += 1
        if isprime(t):
            ans = t
            num += 1
    return ans


def func10():
    for _ in range(0, eval(input())):
        n = eval(input())
        t = fetch(n)
        print(t * t + 1)


func10()