def solve(a,b,a1,b1):
    res = [0]*(a1 + b1)
    for x in range(a1):
        for y in range(b1):
            res[x+y] += a[x]*b[y]
    for i in range(a1+b1):
        res[i] = str(res[i])
    print(' '.join(res))
    return

T = int(input())
x = 0
while(x < T):
    x += 1
    lena,lenb = [int(i) for i in input().split(' ')]
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    solve(a,b,lena,lenb)