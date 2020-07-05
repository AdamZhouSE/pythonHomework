def build(n):
    M = []
    for i in range(n):
        row = list(map(int, input().split()[1:]))
        M.append(row)
    # print(M)
    return M

def traverse(M,queue):
    ans = []
    while len(queue) > 0:
        # print(queue, ans)
        node = queue.pop(0)
        if node in ans:
            continue
        ans.append(node)
        for i in range(len(M)):
            if M[node][i] != 0:
                queue.append(i)
    return ans

def test():
    n,head = input().split()
    nodes = input().split()

    n = int(n)
    head = nodes.index(head)

    M = build(n)
    ans = traverse(M,[head])
    
    for i in range(n):
        ans[i] = nodes[ans[i]]
    return ' '.join(ans)

A = []
for i in range(int(input())):
    A.append(test())

for i in A:
    print(i)