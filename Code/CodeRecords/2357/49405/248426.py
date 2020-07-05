T = int(input())
for t in range(T):
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in range(n):
        if b.count(x - a[i]):
            print('%d %d' % (a[i], x - a[i]))