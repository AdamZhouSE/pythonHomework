class tree:
    fa = -1;
    l = -1
    r = -1
    def __init__(self,faa,ll,rr):
        fa = faa
        l = ll
        r = rr
tr = [tree(-1,-1,-1) for x in range(100005)]
w = [0 for x in range(100005)]
inord  = [0 for x in range(100005)]
lis = [0 for x in range(100005)]
def inorder(root:int,k:list):
    if(tr[root].l!=-1):
        inorder(tr[root].l,k)
    k[0]+=1
    inord[k[0]] =w[root]-k[0]
    if(tr[root].r!=-1):
        inorder(tr[root].r,k)