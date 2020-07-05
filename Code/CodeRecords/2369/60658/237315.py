def pre(parent):
    if parent=="*":
        return 
    ans.append(parent)
    pre(tree[parent][0])
    pre(tree[parent][1])

n = int(input())
tree = {}
ans = []
for i in range(n):
    va,lson,rson=list(input())
    tree[va]=[lson,rson]
pre(list(tree.keys())[0])
print("".join(ans),end="")