T = int(input())
for t in range(T):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = []
    for i in range(0, n, 2):
        b += reversed(a[i:i + 2])
    print(' '.join(map(str, b)))