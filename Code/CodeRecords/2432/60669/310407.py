class Node:
    def __init__(self, item):
        self.item = item
        self.leftChild = None
        self.rightChild = None

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setrightChild(self, rightChild):
        self.rightChild = rightChild

    def __str__(self):
        return self.item


class Tree:
    def __init__(self, root):
        self.root = root

    def __str__(self):
        return self.root


def find(item):
    for i in range(0,len(inorder)):
        if inorder[i]==item:
            return i


def build(startIndex,endIndex,currentRoot,time):   # 后序的index  time是因为后序每一层的中间在最后 所以每往右一层都要整体往左移1个
    inorderIndex=find(currentRoot.item)

    if endIndex-startIndex<2:
        if endIndex-startIndex<=0:
            return
        if inorder[inorderIndex+1]==postorder[endIndex-1]:
            currentRoot.setrightChild(Node(postorder[endIndex-1]))
            return
        else:
            currentRoot.setLeftChild(Node(postorder[endIndex-1]))
            return
    leftStart=startIndex
    leftEnd=inorderIndex-1-time     # endIndex-(endIndex-inorderIndex)-1
    # 括号代表leftLength 这括号里的endIndex本应是中序的endIndex 但中序后序子树长度一样 所以用后序的endIndex没问题
    rightStart=inorderIndex-time    # endIndex-(endIndex-inorderIndex)
    rightEnd=endIndex-1

    leftChild=Node(postorder[leftEnd]) if leftStart<=leftEnd else None
    rightChild=Node(postorder[rightEnd]) if rightStart<=rightEnd else None
    currentRoot.setLeftChild(leftChild)
    currentRoot.setrightChild(rightChild)

    build(leftStart,leftEnd,leftChild,time) if leftChild!=None else None
    build(rightStart,rightEnd,rightChild,time+1) if rightChild!=None else None


def dfs(currentNode,sum):
    if currentNode.leftChild==None and currentNode.rightChild==None:
        return currentNode.item,sum
    else:
        leftSum=1000000
        rightSum=1000000
        if currentNode.leftChild!=None:
            tuple=dfs(currentNode.leftChild,sum+currentNode.leftChild.item)
            leftItem=tuple[0]
            leftSum=tuple[1]
        if currentNode.rightChild!=None:
            tuple = dfs(currentNode.rightChild, sum+currentNode.rightChild.item)
            rightItem = tuple[0]
            rightSum = tuple[1]
        if leftSum<rightSum:
            return leftItem,leftSum
        elif leftSum>rightSum:
            return rightItem,rightSum
        else:
            if leftItem<rightItem:
                return leftItem, leftSum
            else:
                return rightItem, rightSum

if __name__ == '__main__':
    inorder=list(map(int,input().split(" ")))    # 中序遍历
    postorder=list(map(int,input().split(" ")))  # 后序遍历
    root=Node(postorder[-1])
    build(0,len(postorder)-1,root,0)
    tree=Tree(root)
    print(dfs(root,0)[0])