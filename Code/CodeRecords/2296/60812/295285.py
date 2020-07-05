n, root = [int(i) for i in input().split(' ')]
tree = [[0] for i in range(n+1)]
for i in range(n):
    fa, lch, rch, val = [int(i) for i in input().split(' ')]
    tree[lch][0] = tree[rch][0] = fa
    tree[fa].append(val)
sum = int(input())
maxlen = 0
for i in range(1, n+1):
    length, val = 1, tree[i][1]
    while i != root:
        if val == sum:
            maxlen = max(maxlen, length)
        i = tree[i][0]
        val += tree[i][1]
        length += 1
    if val == sum:
        maxlen = max(maxlen, length)
print(maxlen)