from collections import defaultdict
treenode = defaultdict(list)
fa = defaultdict(int)
n_r = input().split(" ")
n = int(n_r[0])
root = int(n_r[1])
list1 = []
for i in range(n):
    f_l_r_v = input().split(" ")
    f = int(f_l_r_v[0])
    list1.append(f)
    l = int(f_l_r_v[1])
    r = int(f_l_r_v[2])
    v = int(f_l_r_v[3])
    treenode[f].append(l)
    treenode[f].append(r)
    treenode[f].append(v)
    fa[l] = f
    fa[r] = f
    if f == root:
        if len(treenode[f]) != 4:
            treenode[f].append(0)
    else:
        if len(treenode[f]) != 4:
            treenode[f].append(treenode[fa[f]][3] + 1)


s = int(input())


count = []
def dfs(dic: defaultdict, root: int, cnt: int):
    if not root:
        return
    cnt += dic[root][2]
    if cnt == s:
        count.append(root)
    dfs(dic, dic[root][0], cnt)
    dfs(dic, dic[root][1], cnt)

max = 0
for i in list1:
    count.clear()
    dfs(treenode, i, 0)
    for x in count:
        if treenode[x][3] - treenode[i][3] > max:
            max = treenode[x][3] - treenode[i][3]
print(max + 1)
