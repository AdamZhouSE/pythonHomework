def dfs(pre,cur):
    global Min,s
    num[cur] = 1
    m = -1
    for to in tree[cur]:
        if to==pre:
            continue
        dfs(cur,to)
        num[cur]+=num[to]
        m = max(m,num[to])
    m = max(m,n-num[cur])
    if m<Min:
        Min = m
        s = 0
        ans[0] = cur
    elif m==Min:
        s+=1
        ans[s] = cur
"""
num[i]:以i为根的子树（即这是子树，并且以i为根）的节点数
状态转移：num[i]=num[j]+1,j属于i的子节点
对于每一个节点来说，只需要考虑两个方面，子树，和上层树
则每个节点的连通分量结点数只要考虑max(num[j],n-num[i]),此处num[j]表示所有的i的子树的结点数
最后比较最小值即可
"""
n = int(input())
Min = 100000
s = 0
tree =dict()
ans = [0 for x in range(100000)]
num = [0 for x in range(n+1)]
for i in range(n-1):
    fro,to = [int(x) for x in input().split()]
    if fro in tree:
        tree[fro].append(to)
    else:
        tree[fro] = [to]
    if to in tree:
        tree[to].append(fro)
    else:
        tree[to] = [fro]
dfs(0,1)
ans = ans[:s+1]
ans.sort()
print(*ans,end=" ")