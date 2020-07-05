T = int(input())
for t in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(0, n, k):
        print(' '.join(map(str, list(reversed(a[i:i + k])))), end=' ')
    print()