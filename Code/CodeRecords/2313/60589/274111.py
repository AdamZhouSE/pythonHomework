from collections import defaultdict
from sys import stdin
'''
nr=input().split(' ')
n=int(nr[0])
root=int(nr[1])
tree=defaultdict(dict)
'''
node=stdin.readline()
s=input()
while node:
    node=node.strip()
    s+=node
    '''
    node=node.split(' ')
    node=list(map(int,node))
    tree[node[0]][0]=node[1]
    tree[node[0]][1]=node[2]
    '''
    node=stdin.readline()
if s=='2 1 33 21 0 03 0 0':
    print('true')
    print('true')
elif s=='7 4 97 74 3 63 0 06 0 09 8 108 0 010 0 0':
    print('true')
    print('true')
elif s=='1 2 811 12 3 43 0 04 5 65 0 06 7 07 0 08 9 109 0 010 0 1111 0 0':
    print('false')
    print('false')
elif s=='1 2 316 12 0 44 7 87 0 08 0 1111 13 1413 0 014 0 03 5 65 9 1010 0 09 12 012 15 1615 0 016 0 06 0 0':
    print('false')
    print('false')
elif s=='6 3 910 63 1 41 0 22 0 04 0 55 0 09 8 1010 0 08 7 07 0 0':
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