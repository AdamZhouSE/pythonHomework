read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    n = read()
    r = []
    for i in range(1, n + 1):
        x = i
        raw = []
        while x:
            raw.append('1' if x % 2 else '0')
            x //= 2
        raw.reverse()
        r.append(''.join(raw))
    print(' '.join(r)+' ')
