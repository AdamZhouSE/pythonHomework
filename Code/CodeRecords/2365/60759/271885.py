ts = int(input())
for t in range(ts):
    n = int(input())
    lst = input().split(' ')
    ans = ''
    for i in range(9, 0, -1):
        n_strs = [s for s in lst if s.startswith(str(i))]
        if len(n_strs) > 1:
            max_len = max([len(s) for s in n_strs])
            n_strs2 = []
            for s in n_strs:
                save = len(s)
                tail = s[-1]
                s += tail * (max_len - save)
                n_strs2.append([s, save])
            n_strs2.sort(reverse=True)
            ans += ''.join(list(map(lambda x: x[0][:x[1]], n_strs2)))
        else:
            ans += ''.join(n_strs)
    print(''.join(ans))
