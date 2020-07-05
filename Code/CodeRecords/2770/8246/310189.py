def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        p = calc(n)
        print(2**p)



def calc(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return calc(n-1) + calc(n-2)

solve()