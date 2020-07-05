def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


def getBoundaryCount(p, q):
    if p[0] == q[0]: return abs(p[1]- q[1]) - 1;
    if p[1] == q[1]: return abs(p[0] - q[0]) - 1;
    return gcd(abs(p[0]- q[0]), abs(p[1] - q[1])) - 1


def getInternalCount(p, q, r):
    BoundaryPoints = getBoundaryCount(p, q) + getBoundaryCount(p, r) + getBoundaryCount(q, r) + 3
    doubleArea = abs(p[0] * (q[1] - r[1]) + q[0]* (r[1] - p[1]) + r[0] * (p[1] - q[1]))
    return (doubleArea - BoundaryPoints + 2) / 2


n = int(input())
for temp in range(n):
    p = input().split(" ")
    for i in range(2): p[i] = int(p[i])
    q = input().split(" ")
    for i in range(2): q[i] = int(q[i])
    r = input().split(" ")
    for i in range(2): r[i] = int(r[i])
    print(int(getInternalCount(p, q, r)))