T = int(input())
for _ in range(T):
    a = [int(x) for x in input().split(' ')]
    x = a[1]
    a = [int(x) for x in input().split(' ')]
    s = 0
    for i in a:
        if i % x == 0:
            s = s | i
    print(s)

