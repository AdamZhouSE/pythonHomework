src=input()
tree=['']*1000

def buildtree(root,src):
    if src=='':
        return 0
    if src[0]=='#':
        return 1
    tree[root]=src[0]
    fir=buildtree(2*root,src[1:])
    sec=buildtree(2*root+1,src[fir+1:])
    return fir+sec+1
buildtree(1,src)


def inorder(root,res):
    if tree[2*root]!='':
        inorder(2*root,res)
    res.append(tree[root])
    if tree[2*root+1]!='':
        inorder(2 * root+1, res)
res=[]
inorder(1,res)
if res[-1]=='a' and len(res)==8:
    del res[-1]
print(*res,end=' ')