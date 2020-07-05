t = eval(input())
for _ in range(t):
    n = eval(input())
    a = [int(x) for x in input().split(' ')]
    k = eval(input())
    r = a[k:] + a[0:k]
    print(' '.join([str(sr) for sr in r])+' ')
