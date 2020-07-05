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
    for i in range(arr.index(0), len(arr)):
        if arr[i] != 0:
            return 'false'
    return 'true'


n, root = map(int, input().split(' '))
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))
a = is_bst(data)
b = is_ct(data)
print(a)
print(b)
if a=='true' and b=='false':
    print(root)
    print(data)
