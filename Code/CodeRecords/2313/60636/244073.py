def out(tree,start,end,a):
    if(start<end):
        a.append(tree[start])
        out(tree,2*start+1,end,a)
        out(tree,2*start+2,end,a)
n_root=input().split(" ")
n=int(n_root[0])
root=int(n_root[1])

