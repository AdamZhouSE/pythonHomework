n=int(input())
edges=eval(input())
def findMin(n,edges):
    if(n<=2):
        return [i for i in range(n)]
    from collections import defaultdict
    from collections import deque
    #表示入度
    in_degrees=[0]*n
    #如果为False表示删除
    res=[True]*n
    adjs=defaultdict(list)
    for edge in edges:
        in_degrees[edge[0]]+=1
        in_degrees[edge[1]]+=1
        adjs[edge[0]].append(edge[1])
        adjs[edge[1]].append(edge[0])

    deque=deque()
    for i in range(n):
        if in_degrees[i]==1:
            deque.append(i)#节点i的入度为1

    while n>2:
        size=len(deque)
        n=n-size
        #减去所有入度为1的点
        for i in range(size):
            top=deque.popleft()
            res[top]=False

            succ=adjs[top]
            succ.append(top)

            for item in succ:
                #相连节点入度减一
                in_degrees[item]-=1

                if in_degrees[item]==1:
                    deque.append(item)

    return [i for i in range(len(res)) if res[i]]

print(findMin(n,edges))