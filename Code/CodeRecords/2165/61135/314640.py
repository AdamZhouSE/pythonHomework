from queue import Queue
nodes=Queue()
T=int(input())
for i in range(0,T):
    a=input().split(" ")
    node=input().split(" ")
    res=list()
    for j in range(0,int(a[0])):
        t=(input().split(" "))[1:]
        t=list(int(x) for x in t)
        res.append(t)
    results=list()
    nodes.put(node.index(a[1]))
    while(len(results)!=int(a[0])):
        id=nodes.get()
        nownode=node[id]
        if nownode not in results:
            results.append(nownode)
        for k in range(len(res[id])):
            if res[id][k]==1:
                nodes.put(k)
                if node[k] not in results:
                    results.append(node[k])
    print(" ".join(results))