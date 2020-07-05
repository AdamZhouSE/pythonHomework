read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]

t = read()
for _ in range(t):
    xs = input()
    dif = [ord(xs[i + 1]) - ord(xs[i]) for i in range(len(xs) - 1)]
    # print(dif)
    diff = [dif[i + 1] - dif[i] for i in range(len(dif) - 1)]
    # print(diff)

    cnt, mv, mi = 0, 0, []
    for i, d in enumerate(diff):
        if not d and dif[i] != 0:
            cnt += 1
            if cnt > mv:
                mv, mi = cnt, [i]
            elif cnt == mv:
                mi.append(i)
        else:
            cnt = 0
    # print(mv, mi)
    mvv, mii = int(1e18), []
    for i in [x + 1 for x in mi]:
        if dif[i] < mvv:
            mvv, mii = dif[i], [i]
        elif dif[i] == mvv:
            mii.append(i)
    # print(mvv, mii)

    mvvv, miii = 0, 0
    for i in [x + 1 for x in mii]:
        if ord(xs[i]) > mv:
            mvvv, miii = xs[i], i
    # print(mvvv, miii)

    x, y = miii, miii - mv - 2
    xx = xs[x:y:-1]
    subs = xs[miii - mv - 1:miii + 1]
    subs = sorted(subs, reverse=True)
    print(''.join(subs))
