t = eval(input())
for _ in range(t):
    n, x = [int(x) for x in input().split()]
    es = [int(x) for x in input().split()]
    l, r, v = 0, 0, 0
    while l < n:
        if v == x:
            print(l + 1, r)
            break
        if v > x or r == n:
            v -= es[l]
            l += 1
        elif v < x:
            v += es[r]
            r += 1
    else:
        print(-1)
