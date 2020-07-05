from collections import defaultdict
treenode = defaultdict(list)
l1 = input().split(" ")
n, r = int(l1[0]), int(l1[1])
res = []
for i in range(n):
    node = input().split(" ")
    treenode[int(node[0])].append(int(node[1]))
    treenode[int(node[0])].append(int(node[2]))
tn = int(input())


def midtravasal(dic: defaultdict, root: int):
    if root == 0:
        return
    midtravasal(dic, dic[root][0])
    res.append(root)
    midtravasal(dic, dic[root][1])


midtravasal(treenode, r)
i = res.index(tn)
if i == len(res) - 1:
    print(0)
else:
    print(res[i + 1])