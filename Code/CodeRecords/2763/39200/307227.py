def cal(start, m, n):
    a = start + 1
    if n == 1:
        return [for i in range(a, m + 1)]
    while a < m / (2 ** (n - 1)):
        cal(2 * a, m, n - 1)
        a += 1
    return


t = int(input())
for x in range(t):
    m, n = [int(i) for i in input().split()]
    cal(0, m, n)
        
