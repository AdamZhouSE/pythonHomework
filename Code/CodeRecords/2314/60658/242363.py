def dfs(root):
    if root==0:
        return
    dfs(tree[root][0])
    ans.append(root)
    dfs(tree[root][1])

n = int(input())
ans = []
tree={}
p,l,r = [int(x) for x in input().split()]
tree[p]=tuple([l,r])
root = p
for i in range(n-1):
    p,l,r = [int(x) for x in input().split()]
    tree[p]=tuple([l,r])
dfs(root)
print(*ans,end=" ")