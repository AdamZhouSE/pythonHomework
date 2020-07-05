m = int(input())
for v in range(0, m):
    l, g, p = map(int, input().split())
    #num = int(input())
    cl = 0
    cg = 0
    while p > 1:
        if l%p == 0:
            l -= 1
            cl += 1
        if g%p == 0:
            g -= 1
            cg += 1
        p -= 1
    print(cl, end='')
    print(' ', end='')
    print(cg)