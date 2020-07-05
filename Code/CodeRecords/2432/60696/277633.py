import sys
lch = []
rch = []
post_order = []
in_order = []
min_sum = sys.maxsize
res = 0


def build(l1,r1,l2,r2):
    if l1 > r1:
        return 0
    root = post_order[r2]
    cnt = 0
    i = l1
    while in_order[i] != root:
        i += 1
        cnt += 1
    lch[root] = build(l1, l1 + cnt - 1, l2, l2+cnt-1)
    rch[root] = build(l1+cnt+1, r1, l2+cnt, r2-1)
    return root


def dfs_with_sum(node, cur_sum):
    global min_sum, res
    cur_sum += node
    if lch[node] == 0 and rch[node] == 0:
        if cur_sum < min_sum or (cur_sum == min_sum and node < res):
            min_sum = cur_sum
            res = node
        return
    if lch[node] != 0:
        dfs_with_sum(lch[node], cur_sum)
    if rch[node] != 0:
        dfs_with_sum(rch[node], cur_sum)
    return


if __name__ == '__main__':
    in_order = [int(i) for i in input().split()]
    post_order = [int(i) for i in input().split()]
    temp = max(in_order)
    lch = [0 for i in range(temp+1)]
    rch = [0 for i in range(temp+1)]
    build(0, len(in_order)-1, 0, len(post_order)-1)
    dfs_with_sum(post_order[-1], 0)
    print(res)