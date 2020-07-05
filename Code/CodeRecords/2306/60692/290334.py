from collections import defaultdict
treenode = defaultdict(list)
l1 = input().split(" ")
n, r = int(l1[0]), int(l1[1])
res, ans = [], []
for i in range(n):
    node = input().split(" ")
    treenode[int(node[0])].append(int(node[1]))
    treenode[int(node[0])].append(int(node[2]))


def midtravasal(dic: defaultdict, root: int):
    if root == 0:
        return
    midtravasal(dic, dic[root][0])
    res.append(root)
    midtravasal(dic, dic[root][1])


def pretravasal(dic: defaultdict, root: int):
    if root == 0:
        return
    res.append(root)
    pretravasal(dic, dic[root][0])
    pretravasal(dic, dic[root][1])


def posttravasal(dic: defaultdict, root: int):
    if root == 0:
        return
    posttravasal(dic, dic[root][0])
    posttravasal(dic, dic[root][1])
    res.append(root)


res.clear()
pretravasal(treenode, r)
res = [str(i) for i in res]
ans.append(" ".join(res))
res.clear()
midtravasal(treenode, r)
res = [str(i) for i in res]
ans.append(" ".join(res))
res.clear()
posttravasal(treenode, r)
res = [str(i) for i in res]
ans.append(" ".join(res))
for j in range(len(ans)):
    if j == len(ans) - 1:
        print(ans[j])
    else:
        print(ans[j] + " ")
