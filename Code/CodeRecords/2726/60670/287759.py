def inrange(t):
    global n
    if t<=n:
        return True
    else:
        return False

def search(root,depth):
    global mindepth
    if depth>=mindepth:
        return
    global tree
    if inrange(root*2):
        if tree[root*2]=="null":
            if inrange(root*2+1):
                if tree[root*2+1]=="null":
                    mindepth=depth
            else:
                mindepth=depth
    else:
        if (inrange(root*2))and(tree[root*2]!="null"):
            search(root*2,depth+1)
        if (inrange(root*2+1))and(tree[root*2+1]!="null"):
            search(root*2+1,depth+1)
    return

tree=input().lstrip('[').rstrip(']').split(',')
n=len(tree)
mindepth=len(tree)
search(0,1)
print(mindepth) 