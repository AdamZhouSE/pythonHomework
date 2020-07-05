import collections
import re
pattern = re.compile('[0-9]+')
a = pattern.findall(input())
n = int(a[0])
root = int(a[1])
tree = [[0, 0] for _ in range(1000000)]
for i in range(n):
    a = [int(x) for x in pattern.findall(input())]
    fa, lch, rch = a[0], a[1], a[2]
    tree[fa][0], tree[fa][1] = lch, rch
queue = collections.deque()
queue.append(root)
res = []
i = 1
count = 1
while queue:
    root_ = queue.popleft()
    count -= 1
    res.append(root_)
    if tree[root_][0] != 0:
        queue.append(tree[root_][0])
    if tree[root_][1] != 0:
        queue.append(tree[root_][1])
    if count == 0:
        count = len(queue)
        print('Level', i, ':', *res)
        res = []
        i += 1
queue.append(root)
res = []
i = 1
count = 1
while queue:
    root_ = queue.popleft()
    count -= 1
    res.append(root_)
    if tree[root_][0] != 0:
        queue.append(tree[root_][0])
    if tree[root_][1] != 0:
        queue.append(tree[root_][1])
    if count == 0:
        count = len(queue)
        if i % 2 != 0:
            print('Level', i, 'from left to right:', *res)
        else:
            print('Level', i, 'from right to left:', *(reversed(res)))
        res = []
        i += 1






