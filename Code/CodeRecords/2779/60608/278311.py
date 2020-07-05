

def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


def func26():
    for _ in range(0, eval(input())):
        n, arr = eval(input()), list(map(int, input().split()))
        a, b = max(arr), min(arr)
        print(a * b // gcd(a, b))


func26()
