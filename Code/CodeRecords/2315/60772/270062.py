n = int(input())
tree = [1] * n
childnum = [0] * n
for i in range(n - 1):
    parent, this = map(int, input().split(" "))
    if childnum[parent] >= 2:
        tree[this] = 0
        childnum[this] = 2
        continue
    tree[this] += tree[parent]
    childnum[parent] += 1
print(max(tree))
