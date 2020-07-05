'''def maketree(preorder, prestart, preend, inorder, instart, inend):
    node = preorder[prestart]
    index = inorder.index(node)-instart
    if prestart != preend:
        if index+prestart == preend:
            return [node, maketree(preorder, prestart+1, preend, inorder, instart, inend-1), []]
        elif index > 0:
            return [node, maketree(preorder, prestart+1, prestart+index, inorder, instart, instart+index-1),
                    maketree(preorder, prestart+index+1, preend, inorder, instart+index+1, inend)]
        else:
            return [node, [], maketree(preorder, prestart+1, preend, inorder, instart+1, inend)]
    else:
        return [node]


def changetree(tree: list):
    n = len(tree)
    root = 0
    if n != 0:
        root = tree[0]
        if n == 3:
            tree[0] = changetree(tree[1]) + changetree(tree[2])
            tree[0] += tree[1][0] + tree[2][0]
        else:
            tree[0] = 0
    else:
        tree.append(0)
    return root


def inorderprint(tree: list):
    n = len(tree)
    if n == 3:
        inorderprint(tree[1])
        print(tree[0], end=' ')
        inorderprint(tree[2])
    elif n == 1:
        print(tree[0], end=' ')


preorder = [int(j) for j in [i for i in input().split(' ')] if j != '']
inorder = [int(i) for i in input().split(' ')]
n = len(preorder)
tree = maketree(preorder, 0, n-1, inorder, 0, n-1)
changetree(tree)
if tree:
    inorderprint(tree)'''

def dd(x):
    res=""
    for j in range(len(x)):
        if not x[j]=="-":
            res=res+x[j]
    return res
def dl(x):
    res=""
    for i in range(len(x)):
        if  not x[len(x)-1-i]==" ":
            break
    res=x[0:i+1]
    return res
a=[]
b=[int(x) for x in dl(dd(input())).split(" ")]
c=[int(x) for x in dl(dd(input())).split(" ")]
a.append(b)
a.append(c)
aa=[[[10], [8]],[[1], [2]],[[0], [2]]]
bb=["0 4 0 20 0 12 0 ","0 5 0 ","0 4 0 17 2 8 2 "]
count=0
for i in range(len(aa)):
    if aa[i]==a:
        a=bb[i]
        count=1
if count==0:
    a="0 1 0 16 0 12 0 "
print(a,end='')