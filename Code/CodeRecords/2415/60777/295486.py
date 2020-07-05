n=int(input())
frac=[int(x) for x in input().split(' ')]
res=[]
def tree(l,r,root,fa):
    if(l==r):
        fa[l]=root
        res.append(fa)
        return 
    if(r<root):
        for i in range(l,r+1):
            tree(l,i-1,i,
        