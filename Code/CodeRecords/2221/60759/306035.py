from collections import defaultdict


def add_all_fans(idol, first_fan):
    vis[first_fan] = True
    for other in fans[first_fan]:
        if not vis[other]:
            if other not in fans[idol]:
                fans[idol].append(other)
            add_all_fans(idol, other)


ns, ms = map(int, input().split(' '))
records = []
fans = defaultdict(list)
for m in range(ms):
    a, b = map(int, input().split(' '))
    if [a, b] not in records:
        records.append([a, b])
        fans[b].append(a)
ans = 0
for cow in list(fans.keys()):
    vis = defaultdict(bool)
    vis[cow] = True
    add_all_fans(cow, cow)
    if len(fans[cow]) == ns - 1:
        ans += 1
print(ans)
