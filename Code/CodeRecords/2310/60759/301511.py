from collections import defaultdict


def solve1(r):
    if r == 0:
        return []
    record = []
    vis = [False for k in range(max(tree.keys()) + 1)]
    queue = [[r, 0]]
    vis[r] = True
    global leaves
    while queue:
        now = queue.pop(0)
        if now[0] != 0:
            record.append(now)
            sub_l = now[1] + 1
            subs = []
            if tree[now[0]] == [0, 0]:
                leaves.append(now[0])
            for i in tree[now[0]]:
                if not vis[i]:
                    vis[i] = True
                    subs.append([i, sub_l])
            queue.extend(subs)
    record.insert(0, [0, -1])
    record.append([0, n])
    ans1, ans2 = [], []
    for i in range(1, len(record)):
        if record[i][1] > record[i - 1][1]:
            ans1.append(record[i][0])
            if record[i - 1][0] not in ans1:
                ans2.append(record[i - 1][0])
    ans1.pop()
    ans2.pop(0)
    ans2.reverse()
    for l in leaves:
        if l not in ans1 and l not in ans2:
            ans1.append(l)
    return ans1 + ans2


def solve2(r):
    global leaves
    ans1 = [r]
    pre = r
    p = tree[pre][0]
    while p not in leaves:
        while p != 0:
            ans1.append(p)
            pre = p
            p = tree[pre][0]
        if pre in leaves:
            break
        p = tree[pre][1]
    ans1.append(p)
    ans2 = []
    pre = r
    p = tree[pre][1]
    while p not in leaves:
        while p != 0:
            ans2.append(p)
            pre = p
            p = tree[pre][1]
        if pre in leaves:
            break
        p = tree[pre][0]
    ans2.append(p)
    for l in leaves:
        if l not in ans1 and l not in ans2:
            ans1.append(l)
    ans2.reverse()
    ans = ans1 + ans2
    while 0 in ans:
        ans.remove(0)
    return ans


def find_ls(r):
    if r == 0:
        return []
    l_c, r_c = tree[r][0], tree[r][1]
    ans = []
    if l_c == 0 and r_c == 0:
        return [r]
    if l_c != 0:
        ans.extend(find_ls(l_c))
    if r_c != 0:
        ans.extend(find_ls(r_c))
    return ans


n, foot = map(int, input().split(' '))
tree = defaultdict(list)
while len(tree) < n:
    fa, lch, rch = map(int, input().split(' '))
    tree[fa] = [lch, rch]
    for ch in [lch, rch]:
        if ch != 0 and ch not in tree:
            tree[ch] = [0, 0]
leaves = find_ls(foot)
print(' '.join(list(map(str, solve1(foot)))) + ' ')
print(' '.join(list(map(str, solve2(foot)))), end=' ')
