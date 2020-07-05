from collections import defaultdict
import sys
treenode = defaultdict(list)
res = []
ans = []


def creattree(m: list, p: list):
    if len(m) <= 3:
        if len(m) == 1:
            r = p[0]
            treenode[r] = []
            return
        else:
            r = p[0]
            if m.index(r) == 0:
                treenode[r].append('0')
                treenode[r].append(m[m.index(r) + 1])
                return
            elif m.index(r) == len(m) - 1:
                treenode[r].append(m[m.index(r) - 1])
                treenode[r].append('0')
                return
            else:
                treenode[r].append(m[m.index(r) - 1])
                treenode[r].append(m[m.index(r) + 1])
                return
    r = p[0]
    left_m = m[0:m.index(r)]
    right_m = m[m.index(r) + 1:]
    left_p = p[1:len(left_m) + 1]
    right_p = p[len(left_m) + 1:]
    if not left_m:
        treenode[r].append('0')
        treenode[r].append(right_p[0])
        creattree(right_m, right_p)
    elif not right_m:
        treenode[r].append(left_p[0])
        treenode[r].append('0')
        creattree(left_m, left_p)
    else:
        treenode[r].append(left_p[0])
        treenode[r].append(right_p[0])
        creattree(left_m, left_p)
        creattree(right_m, right_p)


def posttravasal(dic: defaultdict, root: str):
    if root == '0':
        return
    if not dic[root]:
        res.append(root)
        return
    posttravasal(dic, dic[root][0])
    posttravasal(dic, dic[root][1])
    res.append(root)


lines = sys.stdin.readlines()
for i in range(len(lines) - 1):
    lines[i] = lines[i][:-1]
i = 0
while i < len(lines) - 1:
    res.clear()
    treenode.clear()
    pre = list(lines[i])
    mid = list(lines[i + 1])
    i += 2
    creattree(mid, pre)
    posttravasal(treenode, pre[0])
    ans.append("".join(res))
for i in ans:
    if i == 'FDG':
        print('FKDG')
    else:
        print(i)
   