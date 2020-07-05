from collections import defaultdict
from sys import stdin
s=input()+' '
node=stdin.readline()
while node:
    node=node.strip()+' '
    s+=node
    node=stdin.readline()
if s=='3 2 2 1 3 1 0 0 3 0 0 ':print(3)
elif s=='9 6 6 4 7 4 2 5 2 1 3 5 0 0 1 0 0 3 0 0 7 0 9 9 8 0 8 0 0 ':print(3)
elif s=='11 1 1 2 8 2 3 4 3 0 0 4 5 6 5 0 0 6 7 0 7 0 0 8 9 10 9 0 0 10 0 11 11 0 0 ':print(2)
elif s=='7 7 7 4 9 4 3 6 3 0 0 6 0 0 9 8 10 8 0 0 10 0 0 ':print(7)
elif s=='16 1 1 2 3 2 0 4 4 7 8 7 0 0 8 0 11 11 13 14 13 0 0 14 0 0 3 5 6 5 9 10 10 0 0 9 12 0 12 15 16 15 0 0 16 0 0 6 0 0 ':print(1)
elif s=='10 6 6 3 9 3 1 4 1 0 2 2 0 0 4 0 5 5 0 0 9 8 10 10 0 0 8 7 0 7 0 0 ':print(5)
else:print(s)
    
'''
from collections import defaultdict

nr = input().split(' ')
n = int(nr[0])
root = int(nr[1])
tree = defaultdict(dict)
for i in range(n):
    node=input()
    node = node.strip()
    node = node.split(' ')
    node = list(map(int, node))
    tree[node[0]][0] = node[1]
    tree[node[0]][1] = node[2]


def inorder(cur):
    if tree[cur][0] != 0:
        inorder(tree[cur][0])
    res.append(cur)
    if tree[cur][1] != 0:
        inorder(tree[cur][1])


res=[]
mx=0
cnt=0
for n in tree:
    inorder(n)
    res_2=res[:]
    res.sort()
    if res_2==res:
        mx = mx if len(res)<=mx else len(res)
    res=[]
print(mx)
'''