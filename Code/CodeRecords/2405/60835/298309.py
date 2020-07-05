class node():
    def __init__(self, fa, level):
        self.fa = fa
        self.level = level
n = int(input())
level = [[1]]
nodes = []
for i in range(n):
    nodes.append(node(0, 1))
for i in range(n - 1):
    fa, node = map(int, input().split())
    nodes[node - 1].fa = fa

    for x in range(len(level)):
        if fa in level[x]:
            if x + 1 == len(level):
                level.append([node])
            else:
                level[x + 1].append(node)
            nodes[node - 1].level = x + 1
            break
    #print(level)
print(len(level))
width = 0
for i in level:
    if len(i) > width:
        width = len(i)
print(width)
u, v = map(int, input().split())
len_u = 0
len_v = 0
while u != v:
    #print(u, v)
    u_level = nodes[u - 1].level
    v_level = nodes[v - 1].level
    if u_level > v_level:
        len_u = len_u + 1
        u = nodes[u - 1].fa
    elif u_level < v_level:
        len_v = len_v + 1
        v = nodes[v - 1].fa
    else:
        len_u = len_u + 1
        u = nodes[u - 1].fa
        len_v = len_v + 1
        v = nodes[v - 1].fa
print(2*len_u + len_v, end = "")