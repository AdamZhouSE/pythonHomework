def printM(M):
    print('='*len(M)*3)
    for row in M:
        print(row)
    print('='*len(M)*3)

def build(n,m):
    M = [[0 for i in range(n)] for i in range(n)]
    for i in range(m):
        s,t,w = list(map(int, input().split()))
        s -= 1
        t -= 1
        if M[t][s] == 0 or w < M[t][s]:
            M[t][s] = M[s][t] = w
    return M

def find_path(M,n,s,t):
    nodes = [0 for i in range(n)]
    queue = [s]
    while len(queue) > 0:
        # print('queue %s'%queue)
        n1 = queue.pop(0)
        cands = []
        for n2 in range(n):
            if n2 != s and M[n1][n2] != 0:
                cands.append(n2)
        # print('cands: %s'%cands)
        for n2 in cands:
            temp = nodes[n1] + M[n1][n2]
            if n2 != s and not n2 in queue and nodes[n2] == 0:
                queue.append(n2)
            if nodes[n2] == 0 or temp < nodes[n2]:
                nodes[n2] = temp
        queue = sorted(queue, key=lambda x:nodes[x])
        # print('nodes: %s'%nodes)
    return nodes[t]

n,m,s,t = list(map(int, input().split()))
s -= 1
t -= 1
M = build(n,m)
target = find_path(M,n,s,t)
print(target)