def out(tree,start,end,a):
    if(start<end):
        out(tree,2*start+1,end,a)
        a.append(tree[start])
        out(tree,2*start+2,end,a)
n=int(input())
lists=[]
for i in range(pow(2,n+1)):
    lists.append("*")