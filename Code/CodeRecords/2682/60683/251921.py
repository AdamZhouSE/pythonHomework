T = eval(input())
for i in range(T):
    N, R, L = [int(x) for x in input().split()]
    umask = (1 << L) - (1 << (R - 1))
    res = N | umask
    print(res)