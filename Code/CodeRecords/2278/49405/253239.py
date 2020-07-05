T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        a[i] ^= a[i + 1]
    print(' '.join(map(str, a)))