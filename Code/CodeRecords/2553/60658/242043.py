class node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(root):
    if root==None:
        return 
    dfs(root.left)
    li.append(root.value)

    dfs(root.right)
    
res = 0
n = int(input())
li = []
dp=[0 for i in range(n+1)]
tree = [node(int(x)) for x in input().split()]
tree = [0]+tree
# print(tree)
for i in range(2,n+1):
    fa,ch = [int(x) for x in input().split()]
    if ch==0:
        tree[fa].left = tree[i]
    else:
        tree[fa].right = tree[i]
dfs(tree[1])
li=[0]+li
for i in range(1,n+1):
    li[i]-=i
# print(li)
for i in range(1,n+1):
    dp[i]=1
    for j in range(1,i):
        if li[i]>=li[j]:
            dp[i] = max(dp[i],dp[j]+1)
    #print(dp)
    res=max(res,dp[i])

print(n-res)