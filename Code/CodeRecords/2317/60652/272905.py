a = list(map(int, input().split(',')))
a.sort()
def width(a):
    if len(a) == 1:
        return 0
    n = len(a)
    MIN = 0
    for i in range(n - 1):
        MIN += a[i] * (2 ** (n - 1 - i)-1)
    MAX = 0
    for j in range(1, n):
        MAX += a[j] *( 2 ** j-1)
    return MAX - MIN
print(width(a))