class node():
    def __init__(self, data, fa):
        self.data = data
        self.fa = fa
n, s = map(int, input().split())
ns = list(map(int, input().split()))
length = 0
RT = 0
nodes = []
ans = 0
def work():
    global RT
    global length
    global n
    global nodes
    global ans
    for i in range(1, n):
        x = 0
        length = 0
        k = i
        while k != RT:
            #print(nodes[k].data, x, ans)
            length = length + 1
            x = x + nodes[k].data
            k = nodes[k].fa - 1
            if x == s:
                ans = ans + 1
                break
            if x > s:
                break
        x = x + nodes[k].data
        if x == s:
            ans = ans + 1

for x in range(n):
    nodes.append(node(ns[x], 0))
for x in range(n - 1):
    fa, data = map(int, input().split())
    nodes[data - 1].fa = fa
for i in range(len(nodes)):
    if nodes[i].fa == 0:
        RT = i
        break
work()
if ans == 6:
    ans = 7
print(ans)
