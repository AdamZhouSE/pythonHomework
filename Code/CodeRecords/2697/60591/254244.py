def isValid(tree,strings):
    for x in range(len(strings)):
        if(strings[x]== "null"):
            continue
        now = len(strings) - 1 - x
        father = int((now - 1) / 2)
        if (now % 2 == 0):  # 右子树
            if (int(tree[now]) < int(tree[father])):
                return False
        else:
            if(int(tree[now]) > int(tree[father])):
                return False
    return True


strings = input()[1:-1].split(",")
tree = strings.copy()
strings.reverse()

if(isValid(tree,strings)):
    print("true")
else:
    print("false")