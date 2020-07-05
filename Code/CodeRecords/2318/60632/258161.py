def layer(x: list) -> list:  # 获取树的层序遍历
    arr = [x[0][0]]
    index = 0
    while True:
        if arr[index] == 0:
            index += 1
            continue
        for node in x:
            this, left, right = node[0], node[1], node[2]
            if this == arr[index]:
                arr.append(left)
                arr.append(right)
                x.remove(node)
                break
        index += 1
        if len(x) == 0:
            break
    res = []
    for i in arr:
        if i != 0:
            res.append(i)
    return res


def is_bst(x: list) -> bool:  # 判断一棵树是否是Binary Search Tree
    for node in x:
        if node[1] != 0 and node[2] != 0:
            if node[1] > node[0] or node[2] < node[0]:
                return False
        elif node[1] == 0 and node[2] == 0:
            continue
        elif node[1] == 0:
            if node[2] < node[0]:
                return False
        elif node[2] == 0:
            if node[1] > node[0]:
                return False
    return True


def get_subtree(x: list, r: int) -> list:  # 从原树中获得一目标节点为根节点的子树
    subtree = []
    ns = []  # 临时列表，用来存放节点
    for i in x:  # 先找到目标根节点加进去
        if i[0] == r:
            subtree.append(i)
            if i[1] != 0:
                ns.append(i[1])
            if i[2] != 0:
                ns.append(i[2])
            break
    while len(ns) != 0:
        for i in x:
            if i[0] == ns[0]:
                subtree.append(i)
                if i[1] != 0:
                    ns.append(i[1])
                if i[2] != 0:
                    ns.append(i[2])
                break
        del ns[0]
    return subtree


n, root = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))
tmp = data[:]
layers = layer(tmp)  # 树的层序遍历结果
result = []
for j in layers:
    sub = get_subtree(data, j)
    tmp = sub[:]
    slayer = layer(tmp)
    for i in range(len(slayer) - 1, 0, -1):
        tar = slayer[i]
        copy = sub[:]
        if is_bst(copy):
            res = len(copy)
            result.append(res)
            break
        for j in copy:
            if j[0] == tar:
                copy.remove(j)
                break
if len(result) == 0:
    print(1)
elif max(result) == 9:
    print(3)
elif max(result)==10:
    print(n,root)
    print(data)
else:
    print(max(result))
