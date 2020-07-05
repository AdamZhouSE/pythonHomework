def cal(start, m, n):
    A = []
    a = start
    if n == 1:
        return [[i] for i in range(a, m + 1)]
    while a <= m / (2 ** (n - 1)):
        for i in cal(2 * a, m, n - 1):
            B = [a]
            B.extend(i)
            A.append(B)
        a += 1
    return A


t = int(input())
for x in range(t):
    m, n = [int(i) for i in input().split()]
    print(len(cal(1, m, n)))
