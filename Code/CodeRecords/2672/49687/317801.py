def solve():
    num = int(input())

    for _ in range(num):
        n = int(input())
        calc(n)

def calc(n):
    bn = bin(n)[2:]
    leaf = 32 - len(bn)

    for _ in range(leaf):
        bn = '0' + bn

    rev = ''.join(['0' if i=='1' else '1' for i in bn])

    print(int(rev, 2))
    return

solve()