
def findindex(tree,name):
    for t in range(len(tree)):

        if str(tree[t][0])==str(name):return t
    return -1



def loop(tree,name,sum,length,SUM,lst):
    if name!=0:
        index=findindex(tree,name)
        left=tree[index][1]
        right=tree[index][2]
        sum+=tree[index][3]
        length+=1
        if sum==SUM:lst.append(length)
        loop(tree,left,sum,length,SUM,lst)
        loop(tree, right, sum, length, SUM, lst)

tree=[]
inp=input().split()
root=int(inp[1])
for node in range(int(inp[0])):
    tree.append(list(map(int,input().split())))
sum=int(input())
lst=[]
for node in tree:
    loop(tree,node[0],0,0,sum,lst)
lst.sort(reverse=True)
print(lst[0])



