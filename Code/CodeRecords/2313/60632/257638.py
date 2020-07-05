def is_bst(x: list) -> str:
    for node in x:
        if node[1] != 0 and node[2] != 0:
            if node[1] > node[0] or node[2] < node[0]:
                return 'false'
        elif node[1] == 0 and node[2] == 0:
            continue
        elif node[1] == 0:
            if node[2] < node[0]:
                return 'false'
        elif node[2] == 0:
            if node[1] > node[0]:
                return 'false'
    return 'true'


def is_ct(x: list) -> str:
    arr = [root]
    for node in x:
        this, left, right = node[0], node[1], node[2]
        index = arr.index(this)
        arr.insert(index + 1, left)
        arr.insert(index + 2, right)
    for i in range(arr.index(0), len(arr)):
        if arr[i] != 0:
            return 'false'
    return 'true'


n, root = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))
print(is_bst(data))
print(is_ct(data))
for i in data:
    print(i)
    print(root)
