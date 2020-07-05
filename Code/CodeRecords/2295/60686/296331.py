# 二叉树类
class BTree(object):

    # 初始化
    def __init__(self, data, left=None, right=None):
        self.data = data  # 数据域
        self.left = left  # 左子树
        self.right = right  # 右子树

    # 前序遍历
    def preorder(self):

        if self.data is not None:
            print(self.data, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    # 中序遍历
    def inorder(self, res):

        if self.left is not None:
            self.left.inorder(res)
        if self.data is not None:
            res.append(self.data)
        if self.right is not None:
            self.right.inorder(res)

    # 后序遍历
    def postorder(self):

        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        if self.data is not None:
            print(self.data, end=' ')

    # 层序遍历
    def levelorder(self):

        # 返回某个节点的左孩子
        def LChild_Of_Node(node):
            return node.left if node.left is not None else None

        # 返回某个节点的右孩子
        def RChild_Of_Node(node):
            return node.right if node.right is not None else None

        # 层序遍历列表
        level_order = []
        # 是否添加根节点中的数据
        if self.data is not None:
            level_order.append([self])

        # 二叉树的高度
        height = self.height()
        if height >= 1:
            # 对第二层及其以后的层数进行操作, 在level_order中添加节点而不是数据
            for _ in range(2, height + 1):
                level = []  # 该层的节点
                for node in level_order[-1]:
                    # 如果左孩子非空，则添加左孩子
                    if LChild_Of_Node(node):
                        level.append(LChild_Of_Node(node))
                    # 如果右孩子非空，则添加右孩子
                    if RChild_Of_Node(node):
                        level.append(RChild_Of_Node(node))
                # 如果该层非空，则添加该层
                if level:
                    level_order.append(level)

            # 取出每层中的数据
            for i in range(0, height):  # 层数
                for index in range(len(level_order[i])):
                    level_order[i][index] = level_order[i][index].data

        return level_order

    # 二叉树的高度
    def height(self):
        # 空的树高度为0, 只有root节点的树高度为1
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and self.right is not None:
            return 1 + self.right.height()
        elif self.left is not None and self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    # 二叉树的叶子节点
    def leaves(self):

        if self.data is None:
            return None
        elif self.left is None and self.right is None:
            print(self.data, end=' ')
        elif self.left is None and self.right is not None:
            self.right.leaves()
        elif self.right is None and self.left is not None:
            self.left.leaves()
        else:
            self.left.leaves()
            self.right.leaves()


def searchTree(root_temp, node_f):
    if root_temp is None:
        return False
    if root_temp == node_f:
        return True
    if searchTree(root_temp.left, node_f):
        return True
    return searchTree(root_temp.right, node_f)


def searchLowestCommonAncestor(root_f, node1, node2):
    if root_f == node1 or root_f == node2:
        return root_f
    pInLeft = searchTree(root_f.left, node1)
    qInLeft = searchTree(root_f.left, node2)
    if qInLeft and pInLeft:
        return searchLowestCommonAncestor(root_f.left, node1, node2)
    if (not pInLeft) and (not qInLeft):
        return searchLowestCommonAncestor(root_f.right, node1, node2)
    return root_f


nums, rootNum = (int(x) for x in input().split())
list_all = []
Node_list = []
for i in range(nums):
    list_temp = input().split()
    for j in range(len(list_temp)):
        list_temp[j] = int(list_temp[j])
    list_all.append(list_temp)
q, p = (int(x) for x in input().split())
for i in range(nums):
    Node_list.append(BTree(list_all[i][0]))
for i in range(nums):
    opNode = Node_list[i]
    opNode_inf = list_all[i]
    opNode_left = opNode_inf[1]
    opNode_right = opNode_inf[2]
    for j in range(i, nums):
        if Node_list[j].data == opNode_left:
            opNode.left = Node_list[j]
        elif Node_list[j].data == opNode_right:
            opNode.right = Node_list[j]
for i in Node_list:
    if i.data == p:
        quesnode1 = i
    if i.data == q:
        quesnode2 = i
    if i.data == rootNum:
        root = i

print(searchLowestCommonAncestor(root,quesnode1,quesnode2).data)