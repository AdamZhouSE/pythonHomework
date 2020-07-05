def layer(laye,tree):
    l=[]
    for nodes in laye[len(laye)-1]:

        node=tree[int(nodes)]

        if str(node[1])=='0'and str(node[2])!='0':
            l.append(findindex(tree,node[2]))
        if str(node[2])=='0'and str(node[1])!='0':
            l.append(findindex(tree,node[1]))
        if str(node[1])!='0'and str(node[2])!='0':
            l.append(findindex(tree,node[1]))
            l.append(findindex(tree,node[2]))



    if len(l)>0:
        laye.append(l)
        return True
    else:return False

def findindex(tree,name):
    for t in range(len(tree)):

        if str(tree[t][0])==str(name):return t
    return -1

tree=[]
line1=input().split()
root=line1[1]
for node in range(int(line1[0])):
    tree.append(list(map(int,input().split())))
tree.sort(key=lambda x:x[0])
laye=[[str(findindex(tree,root))]]
while True:
    if not layer(laye,tree):break



for l in range(len(laye)):

    for lll in range(len(laye[l])):
        lll=int(lll)

        laye[l][lll]=tree[int(laye[l][lll])][0]


for l in range(len(laye)):
    print('Level '+str(l+1)+' : '+' '.join(map(str,laye[l])))
for l in range(len(laye)):
        if l%2==1:
            ll=list(laye[l]).copy()
            ll.reverse()

            print('Level '+str(l+1)+' from right to left: '+' '.join(map(str,ll)))
        else:
            print('Level ' + str(l + 1) + ' from left to right: ' + ' '.join(map(str,laye[l])))
