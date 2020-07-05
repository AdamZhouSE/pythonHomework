class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def main(self):
        root = self.buidTree()
        res = self.posOrder(root,[0,0,0])
        print res.val
    def buidTree(self):
        root = TreeNode(6)
        root.left = TreeNode(1)
        root.right = TreeNode(12)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(10)
        root.right.left.left = TreeNode(4)
        root.right.left.left.left = TreeNode(2)
        root.right.left.left.right = TreeNode(5)
        root.right.left.right = TreeNode(14)
        root.right.left.right.left = TreeNode(11)
        root.right.left.right.right = TreeNode(15)
        root.right.right = TreeNode(13)
        root.right.right.left = TreeNode(20)
        root.right.right.right = TreeNode(16)
        return root
    def posOrder(self, root, record):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            record[0] = 0
            record[1] = float("inf")
            record[2] = float("-inf")
            return None
        value = root.val
        left = root.left
        right = root.right
        lBST = self.posOrder(root.left,record)
        lSize = record[0]
        lMin = record[1]
        lMax = record[2]
        rBST = self.posOrder(root.right, record)
        rSize = record[0]
        rMin = record[1]
        rMax = record[2]
        record[1] = min(lMin,value)
        record[2] = max(rMax,value)
        # 只有当左右两个子树的根节点是当前节点的左右子节点，当前节点才能作为根节点加入
        if (not left and not lBST and not right and not rBST) or (left.val == lBST.val and right.val == rBST.val) and lMax < value and value < rMin:
            record[0] = lSize + rSize + 1
            return root
        # 若左右子树不能合并，返回当前最长的那个子树的根节点
        else:
            record[0] = max(lSize,rSize)
            if lSize > rSize:
                return lBST
            else:
                return rBST
s=Solution()
s.main()
