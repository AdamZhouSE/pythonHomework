def in_order(r):
    res = []
    if tree[r][0] != 0:
        res.extend(in_order(tree[r][0]))
    res.append(value[r])
    if tree[r][1] != 0:
        res.extend(in_order(tree[r][1]))
    return res


def find(lst):
    dp = [1 for m in lst]
    for i in range(1, len(lst)):
        choices = []
        for j in range(0, i):
            if lst[j] <= lst[i]:
                choices.append(dp[j])
        if choices:
            dp[i] = 1 + max(choices)
    return max(dp)


n = int(input())
value = list(map(int, input().split(' ')))
value.insert(0, 0)
tree = [[0, 0] for node in range(n + 1)]
for idx in range(2, n + 1):
    fa, ch = map(int, input().split(' '))
    tree[fa][ch] = idx
in_order_lst = in_order(1)
seq = []
for idx in range(len(in_order_lst)):
    seq.append(in_order_lst[idx] - idx)
print(n - find(seq))
