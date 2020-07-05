n = int(input())
a = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]
for i in range(n):
    start = i
    s = a[start]
    vi = [1 for _ in range(n)]
    vi[start] = 0
    while True:
        start = b[start]-1
        if vi[start] == 0:
            break
        else:
            vi[start] = 0
        s += a[start]
    print(s)

