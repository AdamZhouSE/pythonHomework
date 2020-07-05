tests = int(input())

for i in range(tests):
    n = int(input())
    l = list(map(int, input().split()))
    a = 0
    tmp = 0
    pos = l.index(max(l))
    for i in range(pos):
        if tmp < l[i]:
            tmp = l[i]
            continue
        a += tmp - l[i]
    tmp = 0
    for i in range(n - pos - 1):
        if tmp < l[-1-i]:
            tmp = l[-1-i]
            continue
        a += tmp - l[i]
    print(a)

