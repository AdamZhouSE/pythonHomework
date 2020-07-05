class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


n = int(input())
nums = [int(x) for x in input().split()]
root = TreeNode(nums[0])
ans = [-1]


def find(node, fa):
    if node.value < fa.value:
        if fa.left is None:
            fa.left = node
            ans.append(fa.value)
        else:
            find(node, fa.left)
    else:
        if fa.right is None:
            fa.right = node
            ans.append(fa.value)
        else:
            find(node, fa.right)


for i in range(1, n):
    this_node = TreeNode(nums[i])
    find(this_node, root)
for i in ans:
    print(i)