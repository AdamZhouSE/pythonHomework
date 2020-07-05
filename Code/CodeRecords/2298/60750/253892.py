

def solve():
    n = int(input())
    res = []
    nodes = list(map(int,input().split(' ')))
    tree = []
    for i in range(0,n):
        if len(tree) == 0:
            tree.append([nodes[i],0,0])
            res.append(-1)
        else:
            root = tree[0][0]
            j = 0
            while j <len(tree):
                if tree[j][0] == root:
                    if nodes[i] <root:
                        if tree[j][1] == 0:
                            tree[j][1] = nodes[i]
                            tree.append([nodes[i],0,0])
                            res.append(root)
                            break
                        else:
                            root = tree[j][1]
                            j = 0
                    elif nodes[i] > root:
                        if tree[j][2] == 0:
                            tree[j][2] = nodes[i]
                            tree.append([nodes[i],0,0])
                            res.append(root)
                            break
                        else:
                            root = tree[j][2]
                            j = 0
                else:
                    j += 1

    for i in range(0,len(res)):
        print(res[i])

solve()



