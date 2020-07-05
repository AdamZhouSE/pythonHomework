T = int(input())
for t in range(T):
    n = int(input())
    a = input().split()
    d = int(input())
    print(' '.join(a[d:] + a[:d]), end=' ')
    print()