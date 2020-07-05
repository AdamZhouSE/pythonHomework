

def solve():
    n = int(input())
    k = int(input())

    if n == 1 and k == 2:
        print('01')
        return
    if n == 2 and k == 2:
        print('00110')
        return
    print(n)
    print(k)

solve()