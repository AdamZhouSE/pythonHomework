class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


list1=input().split()
list2=input().split()


def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if not postorder:
        return None

    root = TreeNode(postorder[-1])

    root_index = inorder.index(postorder[-1])

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]

    l_left = len(left_inorder)

    left_postorder = postorder[:l_left]
    right_postorder = postorder[l_left: -1]

    root.left = buildTree(left_inorder, left_postorder)
    root.right = buildTree(right_inorder, right_postorder)

    return root

root=buildTree(list1,list2)

list=[]
def find(root,sum):
    sum.append(root.val)
    if root.left==None and root.right==None:
        list.append(sum)
        return
    elif root.left==None:
        temp=[]
        for i in sum:
            temp.append(i)
        find(root.right,temp)
    elif root.right==None:
        temp = []
        for i in sum:
            temp.append(i)
        find(root.left,temp)
    else:
        temp1 = []
        for i in sum:
            temp1.append(i)
        temp2 = []
        for i in sum:
            temp2.append(i)
        find(root.right,temp1)
        find(root.left, temp2)
sum=[]
find(root,sum)

res=0
c=0
for i in  range(len(list)):
    te=0
    for j in list[i]:
        te+=int(j)
    if i==0:
        res=te
        c=int(list[i][-1])
    else:
        if te<res:
            res=te
            c=int(list[i][-1])
        if te==res:
            if int(list[i][-1])<c:
                c=int(list[i][-1])
print(c)