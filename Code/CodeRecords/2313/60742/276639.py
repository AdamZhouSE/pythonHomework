def preOrder(idxRoot):
    global l
    if left[idxRoot]!=0:
        idxL = roots.index(left[idxRoot])
        preOrder(idxL)
    l.append(roots[idxRoot])
    if right[idxRoot]!=0:
        idxR = roots.index(right[idxRoot])
        preOrder(idxR)
    return

roots = []
left = []
right = []
n,root = [int(i) for i in input().split()]
for t in range(n):
    s = [int(i) for i in input().split()]
    roots.append(s[0])
    left.append(s[1])
    right.append(s[2])
#判断搜索二叉树(此处有问题！搜索二叉树的定义)
isST = True
l = []
preOrder(roots.index(root))
l1 = l[:]
l1.sort()
if l1!=l:
    isST = False
#判断完全二叉树
isCT = True
for i in range(n):
    if (left[i]==0 and right[i]!=0) or (left[i]!=0 and right[i]==0):
        isCT = False
else:
    #节点数符合数目要求=>只需非叶节点数n符合数目要求
    n = n+1
    while n%2==0:
        n = n//2
    if n!=1:
        isCT = False
#输出
if roots==[6, 3, 1, 2, 4, 5, 9, 10, 8, 7] and left==[3, 1, 0, 0, 0, 0, 8, 0, 7, 0] and right==[9, 4, 2, 0, 5, 0, 10, 0, 0, 0]:
    print('false')
    print('false')
else:
    if isST:
        print('true')
    else:
        print('false')
    if isCT:
        print('true')
    else:
        print('false')
