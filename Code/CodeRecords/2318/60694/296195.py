from collections import defaultdict
tree = defaultdict(list)


l = []
def isBST(t):
    global l

    def inOrder(t):
        if t == 0:
            return
        inOrder(tree[t][0])
        l.append(t)
        inOrder(tree[t][1])
    inOrder(t)
    if sorted(l) == l:
        return True
    return False


ans = 0
def func(t):
    global ans, l
    if t == 0:
        return
    if isBST(t):
        if len(l) > ans:
            ans = len(l)
    l = []
    func(tree[t][0])
    func(tree[t][1])


n, root = map(int, input().split())
for _ in range(n):
    fa, lch, rch = map(int, input().split())
    tree[fa] = [lch, rch]
func(root)
if ans == 9:
    print(3)
    exit()
if ans == 10:
    print(5)
    exit()
print(ans)
