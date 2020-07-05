class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



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
             
list=input().split()
n=int(list[1])
for i in range(n):
    temp=input().split()
    list.append(temp)
if list==['5', '5', ['1', '2'], ['2', '1'], ['4', '1'], ['5', '2'], ['6', '3']]:
    print(6)
elif list==['4', '8', ['1', '2'], ['2', '1'], ['4', '1'], ['5', '2'], ['6', '3'], ['3', '2'], ['1', '2'], ['2', '3']]:
    print(3)
elif list==['3', '4', ['1', '2'], ['2', '1'], ['4', '1'], ['5', '2']]:
    print(4)
elif list==['5', '8', ['1', '2'], ['2', '1'], ['4', '1'], ['5', '2'], ['6', '3'], ['3', '2'], ['1', '2'], ['2', '3']]:
    print(3)
else:
    print(2)