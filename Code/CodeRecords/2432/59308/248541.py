lch = [-1 for _ in range(10000)]
rch = [-1 for _ in range(10000)]


def dfs(u, my_sum, best_sum, best):
    my_sum += u
    if lch[u] == 0 and rch[u] == 0:
        if my_sum < best_sum or (my_sum == best_sum and u < best):
            best = u
            best_sum = my_sum
    if lch[u] != 0:
        best, best_sum = dfs(lch[u], my_sum, best_sum, best)
    # my_sum -= u
    if rch[u] != 0:
        best, best_sum = dfs(rch[u], my_sum, best_sum, best)
    return best, best_sum


def build(l1, r1, l2, r2):
    if l1 > r1:
        return 0
    root = post[r2]
    p = l1
    while mid[p] != root:
        p += 1
    cnt = p - l1
    lch[root] = build(l1, p-1, l2, l2 + cnt - 1)
    rch[root] = build(p+1, r1, l2+cnt, r2-1)
    return root


mid = [int(x) for x in input().split(' ')]
post = [int(x) for x in input().split(' ')]
build(0, len(mid)-1, 0, len(post)-1)
best, best_sum = dfs(post[-1], 0, 10000000, 0)
print(best)
# [0, 0, 3, 0, 2, 0, 0, 5
# [0, 0, 1, 0, 7, 0, 0, 6,

#



