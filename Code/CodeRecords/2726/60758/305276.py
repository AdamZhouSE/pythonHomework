def deep(tree,depth,current):
    if(current*2+1>len(tree)-1):
        return depth-1
    if tree[current]==-1:
        return depth-1
    return min(deep(tree,depth+1,current*2+1),deep(tree,depth+1,current*2+2))

n=input()
n=n.replace('null','-1')
tree=eval(n)
print(deep(tree,1,0))