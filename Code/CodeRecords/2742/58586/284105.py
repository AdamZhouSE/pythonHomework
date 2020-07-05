import copy


class TreeNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.father=None

    def __str__(self):
        return str(self.value)


def insert(root: TreeNode, node: TreeNode):
    if root.left == None and root.right == None:
        root.right = node
        node.father=root
    else:
        pre=root
        cur=root.right
        while cur != None:
            pre = cur
            if cur.value < node.value:
                cur = cur.right
            else:
                cur = cur.left
        if pre.value > node.value:
            pre.left = node
            node.father=pre
        else:
            pre.right = node
            node.father = pre
    return root


def inorder(root: TreeNode, arr: list):
    if root == None:
        return
    inorder(root.left, arr)
    arr.append(root.value)
    inorder(root.right, arr)


def delete(root: TreeNode,x,arr):
    cur=root.right
    while cur!=None:
        if cur.value==x:
            break
        elif cur.value<x:
            cur=cur.right
        else:
            cur=cur.left
    if cur.left!=None and cur.right!=None:
        succ=find_succ(x,root,arr)
        temp=succ.value
        succ.value=cur.value
        cur.value=temp
        delete_helper(succ)
    else:
        delete_helper(cur)
    return root


def delete_helper(node:TreeNode):
    father=node.father
    if father.left==node:
        if node.right!=None:
            father.left=node.right
            node.right.father=father
        elif node.left!=None:
            father.left=node.left
            node.left.father=father
        else:
            father.left=None
    else:
        if node.right!=None:
            father.right=node.right
            node.right.father=father
        elif node.left!=None:
            father.right=node.left
            node.left.father=father
        else:
            father.right=None


def find_succ(x,root:TreeNode,arr):
    value=get_back(x,arr)
    p=root
    while p!=None:
        if p.value==value:
            break
        elif p.value>value:
            p=p.left
        else:
            p=p.right
    return p


def get_rank(x, arr):
    i = 0
    while i < len(arr) and arr[i] < x:
        i += 1
    return i


def get_num(i,arr):
    return arr[i]


def get_back(x, arr):
    i = 0
    while i < len(arr) and arr[i] <= x:
        i += 1
    result = arr[i] if i < len(arr) else pow(2, 31)
    return result


def get_pre(x, arr):
    i = len(arr) - 1
    while i > 0 and arr[i] >= x:
        i -= 1
    result = arr[i] if i > 0 else pow(-2, 31) + 1
    return result


if __name__ == '__main__':
    operators=int(input())
    roots=[]
    for i in range(operators):
        history,op,num=map(int,input().split(" "))
        arr=[]
        if history==0:
            root=insert(TreeNode(-1),TreeNode(num))
            inorder(root,arr)
            roots.append((root,arr))
        else:
            if op==1 or op==2:
                new_root = copy.deepcopy(roots[history-1][0])
                if op==1:
                    new_root=insert(new_root,TreeNode(num))
                else:
                    new_root=delete(new_root,num,roots[history-1][1].copy())
                inorder(new_root,arr)
                roots.append((new_root,arr))
            else:
                if op==3:
                    print(get_rank(num,roots[history-1][1]))
                elif op==4:
                    print(get_num(num,roots[history-1][1]))
                elif op==5:
                    print(get_pre(num,roots[history-1][1]))
                elif op==6:
                    print(get_back(num,roots[history-1][1]))
                new_root=copy.deepcopy(roots[history-1][0])
                arr=roots[history-1][1].copy()
                roots.append((new_root,arr))

