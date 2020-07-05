class node():
    def __init__(self,left,right):
        self.left = left
        self.right = right
class node():
    def __init__(self,left,right):
        self.left = left
        self.right = right
n, root = map(int, input().split())
nodes = []
level = [[root]]
res = 0
for q in range(n + 1):
    nodes.append(node(0, 0))
def solve(n, o1, o2):
    #print (n)
    global nodes
    global res
    flag = False
    if n == o1:
        flag = True
    elif n == o2:
        flag = True
    elif n == 0:
        return False
    x = nodes[n]
    #print(x.right, x.left)
    r = solve(x.right, o1, o2)
    l = solve(x.left, o1, o2)
    if r and l:
        res = n
        return True
    elif r:
        if flag:
            res = n
        return True
    elif l:
        if flag:
            res = n
        return True
    else:
        return flag
    
    
for x in range(n):
    fa, lch, rch = map(int, input().split())
    nodes[fa].left = lch
    nodes[fa].right = rch
for x in range(int(input())):
    o1, o2 = map(int, input().split())
    res = 0
    solve(root, o1, o2)
    print(res)