from math import log

a = int(input())
n = int(log(a, 2))
tree = []
for i in range(0, n + 1):
    row = [2 ** i + x for x in range(0, 2 ** i)]
    if i % 2 != 0:
        row = row[::-1]
    tree.append(row)
tree = tree[::-1]
pos = tree[0].index(a)
result = [a]
tree = tree[1:]
for row in tree:
    pos //= 2
    result.append(row[pos])
print(result[::-1])
