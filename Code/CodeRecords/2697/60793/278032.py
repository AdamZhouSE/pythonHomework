def judge(x, y, z):
    if x == 'null':
        return True
    elif y == 'null':
        if z == 'null':
            return True
        else:
            return int(x) < int(z)
    elif z == 'null':
        return int(x) > int(y)
    else:
        return int(y) < int(x) < int(z)


tree = list(input()[1:-1].split(","))
result = "true"
for i in range(0, ((len(tree) - 1) - 1 ) // 2):
    node1 = tree[i]
    node2 = tree[(i + 1) * 2 - 1]
    node3 = tree[(i + 1) * 2]
    if not judge(node1, node2, node3):
        result = "false"
print(result)