class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        result = []

        def middle_traversal(root):
            if root.left:
                middle_traversal(root.left)
            result.append(root.val)
            if root.right:
                middle_traversal(root.right)

        middle_traversal(root)
        return result == sorted(result) and len(set(result)) == len(result)


null = 0
nums = eval(input())
first=0
firstNode=TreeNode('firstNode')
for num, index in zip(nums, range(len(nums))):
    if num != 0:
        node = TreeNode(0)
        node.__init__(num)
        high = 0
        count = 0
        for i in range(len(nums)):
            count += 2 ** i
            if count > index:
                high = i
                break
        before = 0
        for i in range(high):
            before += 2 ** i
        position = index - before
        before = count
        left=before + 2 * position
        right=before + 2 * position + 1
        if before + 2 * position < len(nums):
            if nums[left] != 0:
                leftNode=TreeNode(nums[left])
                node.left = leftNode
        if before + 2 * position + 1 < len(nums):
            if nums[right] != 0:
                rightNode=TreeNode(nums[right])
                node.right = rightNode
#        print(num, "high", high, "count", count, "position", position, "left", node.left, "right", node.right)
        if first==0:
            firstNode.val=node.val
            firstNode.left=node.left
            firstNode.right=node.right
            first+=1


t=Solution()
res=t.isValidBST(firstNode)
if res:
    print("true")
else:
    print("false")