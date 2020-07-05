from collections import defaultdict
from collections import deque
def findMinHeightTree(n,edges):
    tmp = [i for i in range(n)]
    if n<=2:
        return tmp
    inDegree=[0]*n
    adja=defaultdict(list)
    for edge in edges:
        adja[edge[0]].append(edge[1])
        adja[edge[1]].append(edge[0])
        inDegree[edge[0]]+=1
        inDegree[edge[1]]+=1
    q=deque()
    for i in range(n):
        if inDegree[i]==1:
            q.append(i)
    leaf=[]
    while n>2:
        n-=len(q)
        for i in range(len(q)):
            fst=q.popleft()
            leaf.append(fst)
            suc=adja[fst]
            for item in suc:
                inDegree[item]-=1
                if inDegree[item]==1:
                    q.append(item)

    res=set(tmp).difference(set(leaf))
    return list(res)


if __name__=="__main__":
    n=int(input())
    edges=eval(input())
    res=findMinHeightTree(n,edges)
    print(res)