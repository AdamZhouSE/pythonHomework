from collections import defaultdict
tree = defaultdict(list)

l = []
def inOrder(t):
    if t == 0:
        return
    inOrder(tree[t][0])
    l.append(t)
    inOrder(tree[t][1])


n = int(input())
root, lch, rch = map(int, input().split())
tree[root] = [lch, rch]
for _ in range(n-1):
    fa, lch, rch = map(int, input().split())
    tree[fa] = [lch, rch]
inOrder(root)
print(*l, end=" ")
