def inrange(t):
    global n
    if t<=n:
        return True
    else:
        return False

def is_node(x):
    global tree
    if not inrange(x):
        return False
    elif tree[x]=="null":
        return False
    return True

def is_leaf(x):
    if (not is_node(x*2+1))and(not is_node(x*2+2)):
        return True
    else:
        return False

def search(root,depth):
    global mindepth
    if depth>=mindepth:
        return
    global tree
    if is_leaf(root):
        mindepth=depth
    else:
        if is_node(root*2):
            search(root*2+1,depth+1)
        if is_node(root*2+1):
            search(root*2+2,depth+1)
    return

tree=input().lstrip('[').rstrip(']').split(',')
n=len(tree)
mindepth=len(tree)
search(0,1)
print(mindepth) 