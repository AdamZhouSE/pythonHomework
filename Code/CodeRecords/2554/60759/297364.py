from collections import defaultdict


def cover(times):
    dots = defaultdict(int)
    for l, r in times:
        dots[l] += 1
        dots[r] -= 1
    s_dots = sorted(dots)
    ans = 0
    cnt = dots[s_dots[0]]
    for d in range(1, len(s_dots)):
        if cnt > 0:
            ans += s_dots[d] - s_dots[d - 1]
        cnt += dots[s_dots[d]]
    return ans


ns = int(input())
ts = []
for n in range(ns):
    ts.append(list(map(int, input().split(' '))))
max_cover = 0
for i in range(len(ts)):
    ts_c = ts.copy()
    ts_c.pop(i)
    max_cover = max(max_cover, cover(ts_c))
print(max_cover, end='')
