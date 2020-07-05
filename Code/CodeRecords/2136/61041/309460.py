import math
def strtoInt(s: str)-> int:
    return int(s)
def isPerfect(n: int) -> int:
    n = int(n)
    h = int(math.log(n, 2))
    p = 2
    l = set()
    l.add(2)
    for i in range(h - 1, 1, -1):
        p = int(pow(n, 1 / i))
        l.add(p)
    for c in l:
        if (n % c == 1):
            u = n * c - n + 1
            t = c
            while (t < u):
                t = t * c

                if t == u: return str(c)
    return str(n - 1)
num = int(input())
print(isPerfect(num))