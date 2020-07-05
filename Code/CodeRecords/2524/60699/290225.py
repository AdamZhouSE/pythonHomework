class node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

input()
list1=list(map(int,input().split(' ')))
root=node(list1[0])
temp=root
for i in range(1,len(list1)):
    cur=list1[i]
    temp=root
    while temp!=None:
        if cur>temp.val:
            if temp.right==None:
                temp.right=node(cur)
                break
            temp=temp.right
        else:
            if temp.left==None:
                temp.left=node(cur)
                break
            temp=temp.left
ans=[]
def dfs(root):
    if root==None:
        return
    ans.append(root.val)
    dfs(root.left)
    dfs(root.right)
dfs(root)
for i in range(0,len(ans)):
    if i!=len(ans)-1:
        print(ans[i],end=" ")
    else:
        print(ans[i],end=" ")