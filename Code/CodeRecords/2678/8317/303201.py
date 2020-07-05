def solve():
    num = int(input())
    bn = ''

    for _ in range(num):
        n = int(input())
        bn = bin(n)[2:]
    
    count = bn.count('1')
    if(count > 1):
        print(-1)
        return

    res = bn[::-1].index('1') + 1
    print(res)


solve()