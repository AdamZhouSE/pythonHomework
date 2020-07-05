read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = int(input())
for _ in range(t):
    n = read()
    xs = read_line()
    xs.append('*')
    have = []
    level = []
    for k, x in enumerate(xs):
        # print(x)
        while x in have or x == '*':
            if not have:
                break
            level.append(len(have))
            have.pop(0)
        have.append(x)
    level = [le * (le + 1) // 2 for le in level]
    print(sum(level))
