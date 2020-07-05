class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def find(numbers,n):
    for i in range(0,len(numbers)):
        if numbers[i]==n:
            return i
    return -1
def creatTree(innum,postnum):
    if len(innum)==0:
        return None
    root=TreeNode(postnum[-1])
    if len(innum)==1:
        return root
    else:
        n=find(innum,root.val)
        root.left=creatTree(innum[0:n],postnum[0:n])
        if n!=len(postnum):
            root.right=creatTree(innum[1+n:],postnum[n:-1])
    return root
def count(res,result,root,sum):
    if root.left==None and root.right==None:
        res.append(sum+root.val)
        result.append(root.val)
    else:
        if root.left!=None:
            count(res,result,root.left,sum+root.val)
        if root.right!=None:
            count(res,result,root.right,sum+root.val)

innum=list(map(int,input().split(" ")))
postnum=list(map(int,input().split(" ")))
root=creatTree(innum,postnum)
res=[]
result=[]
count(res,result,root,0)
i=find(res,min(res))
print(result[i])