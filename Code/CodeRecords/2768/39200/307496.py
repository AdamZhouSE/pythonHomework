t = int(input())
for x in range(t):
    a, b, m = [int(i) for i in input().split()]
    start = 0
    if a % m == 0:
        start = a
    else:
        start = (1 + a // m) * m
    count = 0
    for i in range(start, b + 1, m):
        count += 1
    print(count)
