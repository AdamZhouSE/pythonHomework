read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    yes = [0] * n
    ns = [0] * n
    loc = 0
    for i in range(n):
        while yes[loc]:
            loc += 1
            loc %= n
        for j in range(i + 1):
            loc += 1
            loc %= n
            while yes[loc]:
                loc += 1
                loc %= n
        yes[loc] = 1
        ns[loc] = i + 1
    print(' '.join([str(n) for n in ns]))
