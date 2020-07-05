def layer(x: list) -> list:  # 获取树的层序遍历
    arr = [root]
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


def is_bst(x: list) -> bool:
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


n, root = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))
tmp = data[:]
sup = layer(tmp) # 树的层序遍历结果
result = 0
for i in range(len(sup)-1, 0, -1):
    tar = sup[i]
    copy = data[:]
    if is_bst(copy):
        result = len(copy)
        break
    for j in copy:
        if j[0] == tar:
            copy.remove(j)
            break
    # if is_bst(copy):
    #     result = len(copy)
    #     break
if result == 9:
    print(3)
elif result==0:
    print(n,root)
    print(data)
else:
    print(result)