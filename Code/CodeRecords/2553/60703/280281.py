class tree:

    fa = -1;
    l = -1
    r = -1
    def __init__(self,faa,ll,rr):
        fa = faa
        l = ll
        r = rr
tr = [tree(-1,-1,-1) for x in range(100005)]
w = [0 for x in range(100005)]#节点的数值
inord  = [0 for x in range(100005)]#中序遍历

lis = [0 for x in range(100005)]#最长不降子序列

def inorder(root:int,k:list): #k作为list 只用第一个值，为了按引用传递
    # if(tr[root].l==-1 and tr[root].r==-1):
    #     return
    if(tr[root].l!=-1):
        inorder(tr[root].l,k)
    k[0]+=1
    inord[k[0]] =w[root]-k[0]
    if(tr[root].r!=-1):
        inorder(tr[root].r,k)




n = int(input())
nodes = [int(x) for x in input().split()]
for i in range(1,n+1):
    w[i] = nodes[i-1]
#     根节点的父亲 0
tr[1].fa = 0
for i in range(2,n+1):
    # 读入每一行 t表示左或右儿子
    tr[i].fa,t = [int(x) for x in input().split()]
    if t==0:
        tr[tr[i].fa].l = i
    else:
        tr[tr[i].fa].r = i
k  = [0,0,0]
inorder(1,k)#中序遍历
# 求最长不下降子序列 用w
dp = [0 for x in range(n+1)]
res = 0
for i in range(1,n+1):
    dp[i] = 1
    for j in range(1,i):
        if inord[i]>=inord[j]:
            dp[i] = max(dp[i],dp[j]+1)

    res = max(res,dp[i])
print(n-res)


