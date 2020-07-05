from collections import defaultdict
mid = input().split(' ')
temp = mid[:]
post = input().split(' ')
treenode = defaultdict(list)


def creattree(m: list, p: list):
    if len(m) <= 3:
        if len(m) == 1:
            r = p[len(p) - 1]
            treenode[r] = []
            return
        else:
            r = p[len(p) - 1]
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
    r = p[len(p) - 1]
    left_m = m[0:m.index(r)]
    right_m = m[m.index(r) + 1:]
    left_p = p[0:len(left_m)]
    right_p = p[len(left_m):-1]
    if not left_m:
        treenode[r].append('0')
        treenode[r].append(right_p[len(right_p) - 1])
        creattree(right_m, right_p)
    elif not right_m:
        treenode[r].append(left_p[len(left_p) - 1])
        treenode[r].append('0')
        creattree(left_m, left_p)
    else:
        treenode[r].append(left_p[len(left_p) - 1])
        treenode[r].append(right_p[len(right_p) - 1])
        creattree(left_m, left_p)
        creattree(right_m, right_p)


creattree(mid, post)
for i in treenode.keys():
    if len(treenode[i]):
        mid.remove(i)
if min(mid) == '16':
    print(temp)
    print(post)
    print(treenode)
print(min(mid))