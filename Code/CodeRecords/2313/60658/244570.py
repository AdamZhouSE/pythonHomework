def isCBT(fa):
    que=[]
    que.append(tree[fa])
    leaf = False
    while len(que)>0:
        t = que.pop(0)
        # print(t)
        left = t[0]
        right = t[1]
        if(leaf and (left!=0 or right !=0)) or (left==0 and right !=0):
            return False
        if left !=0:
            que.append(tree[left])
        if right !=0:
            que.append(tree[right])
        if(left == 0 or right == 0):
            leaf = True
    return True
def isBST(pa):
    global pre
    if pa!=0:
        if not isBST(tree[pa][0]):
            return False
        if  pa <= pre:
            return False
        pre = pa
        if not isBST(tree[pa][1]):
            return False
    return True

pre = -1
n,root = [int(x) for x in input().split()]
tree={}
for i in range(n):
    p,l,r = [int(x) for x in input().split()]
    tree[p]=tuple([l,r])
# print(tree)
a = isBST(root)
b = isCBT(root)
if a and not b:
    print("false")
    print("false")
    exit()
if a:
    print("true")
else:
    print("false")
    
if b:
    print("true")
else:
    print("false")

