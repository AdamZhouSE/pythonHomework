n, k = [int(x) for x in input().split(' ')]
info = [('HEAD', 0)]
for _ in range(n):
    tmp = input().split()
    name, mother = tmp[0], int(tmp[1])
    info.append((name, mother))
r_info = [(name, []) for name, mother in info]
for index, (name, mother) in enumerate(info):
    r_info[mother][1].append(index)
for _ in range(k):
    pass
    s = input()[::-1]
    matched = [0] * len(s)
    loc, cnt, nodes = 0, 0, [1]
    while nodes:
        node = nodes.pop()
        v = info[node][0]
        for i in range(len(s) - 1, -1, -1):
            x = matched[i-1]
            y = s[i]
            matched[i] = 1 if (i == 0 or matched[i - 1]) and s[i] == v else 0
        # print(matched)
        if matched[-1]:
            matched[-1] = 0
            cnt += 1
        nodes.extend(r_info[node][1])
    print(cnt)
