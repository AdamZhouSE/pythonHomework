from collections import defaultdict
from copy import deepcopy


def judge(l, r, s, t):
    queue = [[[s], []]]
    choices = []
    while queue:
        p = queue.pop(0)
        tail = p[0][-1]
        for nex in links[tail]:
            now = deepcopy(p)
            if nex not in p[0]:
                now[0].append(nex)
                now[1].append(roads[tuple(sorted((tail, nex)))])
                if nex == t:
                    choices.append(now)
                else:
                    queue.append(now)
    for choice in choices:
        seq = choice[1]
        s_seq = sorted(seq)
        if s_seq == seq and l <= s_seq[0] and s_seq[-1] <= r:
            return True
    return False


# 城市数、道路数、询问数
ns, ms, qs = map(int, input().split(' '))
roads = defaultdict(int)
links = defaultdict(list)
for m in range(1, ms + 1):
    n1, n2 = map(int, input().split(' '))
    roads[tuple(sorted((n1, n2)))] = m
    links[n1].append(n2)
    links[n2].append(n1)
for q in range(qs):
    li, ri, si, ti = map(int, input().split(' '))
    print('Yes' if judge(li, ri, si, ti) else 'No')
