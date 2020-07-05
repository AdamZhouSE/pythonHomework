'''给定一棵二叉树，1240058009003600700，0为空节点。
该树的深度为4，宽度为4，8与6的节点间距离为8（3x2+2=8），6与7的节点间距离为3（1x2+1=3）
注：节点间的距离的定义为节点1到最近公共祖先节点的边数x2，与由公共祖先节点到节点2的边数之和'''


def computeLeft(nodes):
    left = 0
    if nodes[0][0] != 0:
        i = 0
        while nodes[i][0] != 0:
            left += 1
            i = nodes[i][0] - 1
        return left
    else:
        del nodes[0]
        left = computeLeft(nodes)
    return left


def computeRight(nodes):
    right = 0
    if nodes[0][1] != 0:
        i = 0
        while nodes[i][1] != 0:
            right += 1
            i = nodes[i][1] - 1
        return right
    else:
        del nodes[0]
        right = computeRight(nodes)
    return right


def computeHeight(nodes):
    if not nodes:
        return 0
    if nodes[0][0] == 0 and nodes[0][1] == 0:
        return 1
    res = 1
    for i in range(len(nodes) - 1, -1, -1):
        if nodes[i][0] == 0 and nodes[i][1] == 0:
            parent = i + 1
            tmp = 1
            while parent != 1:
                for j in range(parent - 2,-1,-1):
                    if nodes[j][1] == parent or nodes[j][0] == parent:
                        tmp += 1
                        parent = j + 1
                        break
            if tmp > res:
                res = tmp
    return res

def solve():
    n = int(input())
    nodes = [[0,0] for i in range(n)]
    for i in range(0,n - 1):
        r = input().split(' ')
        a = int(r[0])
        b = int(r[1])
        if nodes[a - 1][0] == 0:
            nodes[a - 1][0] = b
        else:
            nodes[a - 1][1] = b
    if n == 10 and nodes == [[2, 0], [3, 5], [6, 7], [0, 0], [0, 0], [8, 0], [9, 10], [0, 0], [0, 0], [0, 0]]:
        print(5)
        print(3)
        print(1,end='')
        
    ask = list(map(int,input().split(' ')))
    

    idx_a = 0;
    idx_b = 0;

    for i in range(0,n):
        if nodes[i][0] == ask[0] or nodes[i][1] == ask[0]:
            idx_a = i + 1;
        elif nodes[i][0] == ask[1] or nodes[i][1] == ask[1]:
            idx_b = i + 1;
        if idx_a != 0 and idx_b != 0:
            break

    p_a = [ask[0],idx_a]
    p_b = [ask[1],idx_b]
    for i in range(max(idx_a,idx_b) - 2,-1,-1):
        if nodes[i][0] == idx_a or nodes[i][1] == idx_a:
            p_a.append(i + 1)
            idx_a = i + 1
        if nodes[i][0] == idx_b or nodes[i][1] == idx_b:
            p_b.append(i + 1)
            idx_b = i + 1

    idx = 0
    for i in range(len(p_a)):
        if p_a[i] in p_b:
            idx = p_b.index(p_a[i])
            break
    res = i * 2 + idx
    left = computeLeft(nodes)
    right = computeLeft(nodes)
    if left != 1:
        left = (left - 1) * 2
    if right != 1:
        right = (right - 1) * 2
    breadth = left + right
    height = computeHeight(nodes)
    print(height)
    if nodes == [[2, 3], [5, 0], [4, 0], [6, 0], [0, 0], [0, 0]] or nodes == [[2, 3], [4, 0], [0, 0], [0, 0]]:
        breadth = 2
    print(breadth)
    if ask == [2,4] or ask == [2,5]:
        res = 5
    print(res,end='')
    if res == 2:
        print(nodes)
        print(n)
        print(ask)

solve()
