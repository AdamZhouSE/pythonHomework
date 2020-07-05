T = int(input())
for t in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for num in a:
        if num != 0:
            b.append(num)
    while len(b) < n:
        b.append(0)
    print(' '.join(map(str, b)), end=' \n')