from collections import defaultdict
n_r = input().split(' ')
n = int(n_r[0])
r = int(n_r[1])
ans = []
treenode = defaultdict(list)
for i in range(n):
    f_l_r = input().split(' ')
    f = int(f_l_r[0])
    lc = int(f_l_r[1])
    rc = int(f_l_r[2])
    treenode[f].append(lc)
    treenode[f].append(rc)
q = [r]
while q:
    ans.append(q)
    next = []
    for i in q:
        left = treenode[i][0]
        right = treenode[i][1]
        if left:
            next.append(left)
        if right:
            next.append(right)
    q = next[:]
for i in range(len(ans)):
    ans[i] = [str(j) for j in ans[i]]
    print("Level "+str(i + 1)+" : "+" ".join(ans[i]))
for j in range(len(ans)):
    if j % 2 == 0:
        print("Level "+str(j + 1)+" from left to right: "+" ".join(ans[j]))
    else:
        ans[j].reverse()
        print("Level "+str(j + 1)+" from right to left: "+" ".join(ans[j]))
