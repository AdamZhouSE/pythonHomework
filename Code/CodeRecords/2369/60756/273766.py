from collections import defaultdict
n=int(input())
if n>0:
    LeftTree=defaultdict(str)
    RightTree=defaultdict(str)
    x0, l, r = tuple(list(input()))
    LeftTree[x0] = l
    RightTree[x0] = r
    for i in range(1,n):
        x,l,r=tuple(list(input()))
        LeftTree[x]=l
        RightTree[x]=r
    ans=[]
    def prefixFind(x:str):
        ans.append(x)
        if LeftTree[x]!='*':prefixFind(LeftTree[x])
        if RightTree[x]!='*':prefixFind(RightTree[x])
    prefixFind(x0)
    print(''.join(ans),end="")