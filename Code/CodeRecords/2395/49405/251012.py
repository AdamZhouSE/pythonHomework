T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1):
        if a[i] == a[i + 1] and a[i] != 0:
            a[i] *= 2
            a[i + 1] = 0
    b = []
    for num in a:
        if num != 0:
            b.append(num)
    while len(b) < n:
        b.append(0)
    print(' '.join(map(str, b)), end='\n')