maxDia = 0

def getHeight(node: int, parent: int, tree_conj: [[int]]):
    global maxDia
    res = []
    for neighbor in tree_conj[node]:
        if neighbor != parent:
            res.append(getHeight(neighbor, node, tree_conj))
    if len(res) == 0:
        return 1
    while len(res) < 2:
        res.append(0)
        res.append(0)
    res = sorted(res)
    maxDia = max(maxDia, sum(res[-2:]))
    return 1 + max(res)

def solve() :
    global maxDia
    res = 0
    x = input().strip().split()
    n = int(x[0])
    m = int(x[1])
    tree_conj = [[] for i in range(n+m)]
    # tree1: 0-n-1, tree2: n-(n+m-1)
    # tree1: i-1
    # tree2: n+i-1
    for i in range(n-1):
        x = input().strip().split()
        a = int(x[0])
        b = int(x[1])
        tree_conj[a-1].append(b-1)
        tree_conj[b-1].append(a-1)
    for i in range(m-1):
        x = input().strip().split()
        a = int(x[0])
        b = int(x[1])
        tree_conj[a+n-1].append(b+n-1)
        tree_conj[b+n-1].append(a+n-1)
    # print(tree_conj)
    for i in range(n):
        for j in range(n, n+m):
            # conj i, j
            # print(i, j)
            tree_conj[i].append(j)
            tree_conj[j].append(i)
            # print(tree_conj)
            maxDia = 0
            getHeight(0, -1, tree_conj)
            tree_conj[i].pop()
            tree_conj[j].pop()
            res += maxDia
            # print(maxDia)
    print(res)

if __name__ == '__main__':
    solve()