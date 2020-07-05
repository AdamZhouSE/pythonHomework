from collections import defaultdict


def judge_s(r, upper=float('inf'), lower=float('-inf')):
    if not r:
        return True
    if r >= upper or r <= lower:
        return False
    l_c, r_c = tree[r]
    if not judge_s(l_c, r, lower):
        return False
    if not judge_s(r_c, upper, r):
        return False
    return True


ns, root = map(int, input().split(' '))
tree = defaultdict(list)
while len(tree) < ns:
    fa, lch, rch = map(int, input().split(' '))
    tree[fa] = [lch, rch]
    for ch in [lch, rch]:
        if ch != 0 and ch not in tree:
            tree[ch] = [0, 0]
queue = [root]
seq = []
while queue:
    current = queue.pop(0)
    if current == 0:
        break
    seq.append(current)
    queue.extend(tree[current])
print('true' if judge_s(root) else 'false')
print('true' if len(seq) == ns else 'false')
