ans = []
def dfs(root):
    left = tree[root][0]
    right = tree[root][1]
    if left!=0:
        dfs(left)
    ans.append(root)
    if right!=0:
        dfs(right)


N = int(input())
tree = dict()
root = 0
for i in range(N):

    f,l,r  = [int(x) for x in input().split()]
    if i==0:
        root = f
    tree[f] = tuple([l,r])
dfs(root)
# print(" ".join([str(x) for x in ans]),end=" ")
print(*ans,end=" ")
