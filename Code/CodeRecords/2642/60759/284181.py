lst = sorted(list(map(int, input().split(','))))
mx = max(lst) - min(lst) + 1 - len(lst)
mx -= min(lst[-1] - lst[-2] - 1, lst[1] - lst[0] - 1)
mi = mx
for l in range(lst[0], lst[-1] - len(lst) + 2):
    cost = len(lst)
    linked = True
    for r in range(l, len(lst) + l):
        if r in lst:
            cost -= 1
        if l < r < l + len(lst) - 1 and r not in lst:
            linked = False
    if linked:
        cost = 2
    mi = min(mi, cost)
print([mi, mx])
