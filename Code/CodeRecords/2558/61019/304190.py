read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs = input()
    v, cnt = 0, 0
    for x in xs:
        if x == '{':
            v += 1
        if x == '}':
            v -= 1
            if v == -1:
                v = 1
                cnt += 1
    if v % 2:
        print(-1)
        continue
    else:
        cnt += v // 2
        print(cnt)
