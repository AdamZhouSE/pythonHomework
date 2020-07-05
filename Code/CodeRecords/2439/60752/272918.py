
def findindex(tree,name):
    for t in range(len(tree)):

        if str(tree[t][0])==str(name):return t
    return -1

def loop(tree,start,end,value):
    if start==end:return value
    start_node=tree[findindex(tree,start)]
    value=value^start_node[2]
    return loop(tree,str(start_node[1]),end,value)


tree=[]
for node in range(int(input())-1):
    tree.append(list(map(int,input().split())))
for r in range(int(input())):
    inp=list(input().split())
    start=inp[0]
    end=inp[1]
    print(loop(tree,start,end,0))
