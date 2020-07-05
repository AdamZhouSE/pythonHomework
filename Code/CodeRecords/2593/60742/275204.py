from itertools import combinations
t = int(input())
for k in range(t):
    n = int(input())
    if k==0:
        a = [int(i) for i in input().split(',')]
    else:
        a = [int(i) for i in input().split()]
    ans_list = []
    l = list(combinations(a,4))
    for i in l:
        l_v = list(i)
        l_v.sort()
        idx = [None]*4
        if l_v[0]+l_v[3]==l_v[1]+l_v[2]:
            for j in range(4):
                idx[j] = a.index(l_v[j])
            min_idx = min(idx)
            min_idx_num = idx.index(min_idx)
            res = []
            res.append(str(min_idx))
            res.append(str(idx[3-min_idx_num]))
            idx.remove(idx[3-min_idx_num])
            idx.remove(min_idx)
            idx.sort()
            res.append(str(idx[0]))
            res.append(str(idx[1]))
            ans_list.append(res)
    if not ans_list:
        print('no pairs')
    else:
        ans_list.sort()
        print(' '.join(ans_list[0]))