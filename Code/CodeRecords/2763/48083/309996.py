def solve():
    num = int(input())

    for _ in range(num):
        m, n = [int(i) for i in input().split(' ')]
        res = calc(m, n)
        print(res)


def calc(m, n):

    if m < n:
        return 0

    if n == 0:
        return 1

    res = (calc(m-1, n) +
           calc(m//2, n-1))
    return res

solve()