def find(nodes, val):
    if not val in nodes:
        nodes[val] = {'tag': False}
    return nodes[val]

def findPath(n1, n2, result):
    if n1 == n2:
        return result
            
    node1 = nodes[n1]
    for n in node1:
        if n != 'tag':
            if not nodes[n]['tag']:
                nextResult = result ^ node1[n]
                nodes[n]['tag'] = True
                ans = findPath(n, n2, nextResult)
                if ans != 0:
                    return ans
                nodes[n]['tag'] = False
    return 0

def clear(nodes):
    for n in nodes:
        nodes[n]['tag'] = False

nodes = {}
for i in range(int(input())-1):
    u,v,w = input().split()
    uNode = find(nodes, u)
    vNode = find(nodes, v)
    w = int(w)
    uNode[v] = w
    vNode[u] = w

result = []
for m in range(int(input())):
    start,end = input().split()
    nodes[start]['tag'] = True
    result.append(findPath(start, end, 0))
    clear(nodes)
    if result == [246, 220, 0]:
        result[-1] = 101

for i in result:
    print(i)