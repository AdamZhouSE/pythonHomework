if __name__ == '__main__':
    n, s = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = sorted(a)

    # print(n, s)
    # print(a, b)
    tag = [0] * n
    loops = []
    for k, v in enumerate(a):
        if tag[k] or v == b[k]:
            tag[k] = 1
            continue

        last = k
        loops.append([])
        cur_loop = loops[-1]
        while True:
            cur_loop.append(last)
            tag[last] = 1
            try:
                last = [i for i in range(n) if b[i] == a[last] and not tag[i]][0]
            except IndexError:
                break

    if sum([len(loop) for loop in loops]) > s:
        print(-1)
        exit(0)

    print(len(loops))
    for loop in loops:
        print(len(loop))
        print(' '.join([str(ind + 1) for ind in loop]), '')
