from collections import defaultdict
def findMHT(edges:[[int]],n):
    if not edges:
        return [0]
    dic=defaultdict(list)
    for x,y in edges:
        dic[x].append(y)
        dic[y].append(x)
    leaves=[i for i in dic if len(dic[i])==1]  # 找到所有叶子结点
    while n>2:
        n-=len(leaves)
        nleave=[]  # 每个结点删掉它连接的叶节点之后如果是新的叶节点则存入
        for l in leaves:
            tmp=dic[l].pop()
            dic[tmp].remove(l)
            if len(dic[tmp])==1:
                nleave.append(tmp)
        leaves=nleave  # 新的一层叶节点
    return leaves

n=int(input())
edges=eval(input())
print(findMHT(edges,n))