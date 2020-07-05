class node():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
    
n, root = map(int, input().split())
nodes = []
for q in range(n + 1):
    nodes.append(node(0, 0, 0))
for q in range(n):
    fa, lch, rch, val = map(int, input().split())
    #print(fa, lch, rch, val)
    nodes[fa] = node(val, lch, rch)
target = int(input())
#print(target)
res = -1
def solve(x, length, now):
    global nodes
    global res
    if x == nodes[0]:
        return
    length = length + 1
    now = now + x.val
    if now == target:
        res = max(length, res)
    #print(x.left, x.right, now)
    solve(nodes[x.left], length, now)
    solve(nodes[x.right], length, now)
for i in range(1, len(nodes)):
    solve(nodes[i], 0, 0)
print(res)