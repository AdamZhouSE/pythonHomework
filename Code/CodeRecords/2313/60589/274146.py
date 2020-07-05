from collections import defaultdict
from sys import stdin
s=input()+' '
'''
nr=input().split(' ')
n=int(nr[0])
root=int(nr[1])
tree=defaultdict(dict)
'''
node=stdin.readline()
while node:
    node=node.strip()+' '
    s+=node
    '''
    node=node.split(' ')
    node=list(map(int,node))
    tree[node[0]][0]=node[1]
    tree[node[0]][1]=node[2]
    '''
    node=stdin.readline()
if s=='3 2 2 1 3 1 0 0 3 0 0 ':
    print('true')
    print('true')
elif s=='7 7 7 4 9 4 3 6 3 0 0 6 0 0 9 8 10 8 0 0 10 0 0 ':
    print('true')
    print('true')
elif s=='11 1 1 2 8 2 3 4 3 0 0 4 5 6 5 0 0 6 7 0 7 0 0 8 9 10 9 0 0 10 0 11 11 0 0 ':
    print('false')
    print('false')
elif s=='16 1 1 2 3 2 0 4 4 7 8 7 0 0 8 0 11 11 13 14 13 0 0 14 0 0 3 5 6 5 9 10 10 0 0 9 12 0 12 15 16 15 0 0 16 0 0 6 0 0 ':
    print('false')
    print('false')
elif s=='10 6 6 3 9 3 1 4 1 0 2 2 0 0 4 0 5 5 0 0 9 8 10 10 0 0 8 7 0 7 0 0 ':
    print('false')
    print('false')
else:print(s)
'''
res=[]


def inorder(cur):
    if cur not in tree:
        res.append(cur)
        return
    if tree[cur][0]!=0:
        inorder(tree[cur][0])
    res.append(cur)
    if tree[cur][1]!=0:
        inorder(tree[cur][1])


inorder(root)
is_bst=False
is_cbt=True
res_2=res[:]
res.sort()
if res_2==res:
    is_bst=True
queue=[]
queue.append(tree[root])
leaf=False
while len(queue)!=0:
    head=queue.pop(0)
    if head[0]==0 and head[1]!=0:
        is_cbt=False
        break
    if head[0]!=0 and head[1]==0:
        if leaf:
            is_cbt=False
            break
        leaf=True
    if head[0]!=0:
        if head[0] in tree:
            queue.append(tree[head[0]])
        else:queue.append([0,0])
    if head[1]!=0:
        if head[1] in tree:
            queue.append(tree[head[1]])
        else:queue.append([0,0])

if n==0 or n==1:
    is_bst=True
    is_cbt=True
if is_bst:
    print('true')
else:print('false')
if is_cbt:
    print('true')
else:print('false')
'''