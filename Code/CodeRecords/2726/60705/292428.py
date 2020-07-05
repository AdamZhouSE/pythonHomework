# leetcode 111 二叉树的最小深度
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        children = [root.left, root.right]
        if not any(children):
            return 1
        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(min_depth, self.minDepth(c))
        return min_depth + 1


def makeTree(node, index):
    try:
        if li[2*index + 1] != "null":
            node.left = TreeNode(li[2*index + 1])
    except IndexError:
        return
    makeTree(node.left, 2*index+1)
    try:
        if li[2*index + 2] != "null":
            node.right = TreeNode(li[2*index + 2])
    except IndexError:
        return
    makeTree(node.right, 2*index + 2)


if __name__ == '__main__':
    li = input()[1:-1].split(",")
    r = TreeNode(li[0])
    makeTree(r, 0)
    solution = Solution()
    print(solution.minDepth(r))

