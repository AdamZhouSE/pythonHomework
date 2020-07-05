class BinaryTree:
    def __init__(self, root):
        self.data = root
        self.left = None
        self.right = None
    def preorder(self):
        if self.data != None:
            print(self.data, end=' ')
        if self.left != None:
            self.left.preorder()
        if self.right != None:
            self.right.preorder()
        # 中序遍历
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        if self.data != None:
            print(self.data, end=' ')
        if self.right != None:
            self.right.inorder()
        # 后序遍历
    def postorder(self):
        if self.left != None:
            self.left.postorder()
        if self.right != None:
            self.right.postorder()
        if self.data != None:
            print(self.data, end=' ')

def Test():
    middle = eval("[" + input().strip().replace(" ", ",") + "]")
    latter = eval("[" + input().strip().replace(" ", ",") + "]")
    tree=GetTwoTree(latter,middle)
    path=[]
    allpath=[]
    def find(tree):
        if(tree==None):
            return
        path.append(tree.data)
        if(tree.left==None and tree.right==None):
            allpath.append(tuple(path))
        find(tree.left)
        find(tree.right)
        path.pop()
        return
    find(tree)
    allpath.sort(key=lambda x:(sum(x),x[-1]))
    print(allpath[0][-1])

def GetTwoTree(str1, str2):  # str1为后序  str2为中序
    root = BinaryTree(str1[-1])  # 先给第一个值
    Index = str2.index(root.data)  # 根在中序中的索引
    leftstr2 = str2[: Index]  # 中序中的左半部分
    maxindex = -1
    for i in leftstr2:  # 分离后序序列
        tmpindex = str1.index(i)
        if maxindex < tmpindex:
            maxindex = tmpindex
    if len(leftstr2) == 1:  # 如果只有一个元素
        root.left = BinaryTree(leftstr2[0])  # 直接赋值
    elif len(leftstr2) == 0:  # 如果没有元素
        root.left = None  # 空
    else:  # 否则递归
        root.left = GetTwoTree(str1[:maxindex + 1], leftstr2)  # 递归构造左子树
    rightstr2 = str2[Index + 1:]  # 中序中的左半部分
    if len(rightstr2) == 1:
        root.right = BinaryTree(rightstr2[0])
    elif len(rightstr2) == 0:
        root.right = None
    else:
        root.right = GetTwoTree(str1[maxindex + 1:-1], rightstr2)  # 递归构造右子树
    return root
if __name__ == "__main__":
    Test()