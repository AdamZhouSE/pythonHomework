def inrange(x):
    global tree,n
    if x>=n or tree[x]==None:
        return False
    return True

def search(x):
    global tree
    l=True
    r=True
    if inrange(x*2+1):
        if tree[x]<tree[x*2+1]:
            return False
        l=search(x*2+1)
    if inrange(x*2+2):
        if tree[x]>tree[x*2+2]:
            return False
        r=search(x*2+2)
    if not (l and r):
        return False
    else:
        return True
           
tree=input().lstrip('[').rstrip(']').split(',')
n=len(tree)
for i in range(0,n):
    if tree[i]=="null":
        tree[i]=None
    else:
        tree[i]=int(tree[i])
print(search(0))