t = int(input())
for i in range(t):
    n = int(input())
    d = 7
    current = 1
    start = 3
    while current != n:
        start += d
        d += 4
        current += 1
    print(start)
