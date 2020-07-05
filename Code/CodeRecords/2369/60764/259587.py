def inorder(tree,i):
    print(tree[i][0],end="")
    if tree[i][1]!="*":
        j=0
        while j<len(tree):
            if tree[j][0]==tree[i][1]:
                break
            j+=1
        inorder(tree,j)
    if tree[i][2]!="*":
        j=0
        while j<len(tree):
            if tree[j][0]==tree[i][2]:
                break
            j+=1
        inorder(tree,j)

n=int(input())
tree=[]
for i in range(n):
    tree.append(input())
inorder(tree,0)