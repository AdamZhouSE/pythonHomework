def findOrder(n,prere):
    degree={}  # the number of cu before it
    for i in range(n):
        degree[i]=0
    adjc={}  # for the next curriculum
    for r in prere:
        adjc.setdefault(r[1],[]).append(r[0])
        degree[r[0]]+=1
    queue=[]  # for all the cus that can be the first one
    for i in range(n):
        if degree[i]==0:
            queue.append(i)
            degree[i]=-1
    res=[]
    while queue:
        node=queue.pop(0)
        res.append(node)
        if node not in adjc:
            # this cu doesn't have to be any other's prerequisite
            continue
        for r in adjc[node]:
            degree[r]-=1
            if degree[r]==0:
                queue.append(r)
                degree[r]=-1
    return res if len(res)==n else []


n=int(input())
prere=eval(input())
print(findOrder(n,prere))