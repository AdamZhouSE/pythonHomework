class Tree:
    val = 0
    left = None
    right = None

    def __init__(self, x):
        self.val = x


num = int(input())
nums = list(map(int, input().split(" ")))
root = Tree(nums[0])
print(-1)

def insert(root, val):
    if val < root.val:
        if root.left is None:
            root.left = Tree(val)
            return root.val
        else:
            return insert(root.left, val)
    if val > root.val:
        if root.right is None:
            root.right = Tree(val)
            return root.val
        else:
            return insert(root.right, val)


for i in range(1, num):
    print(insert(root, nums[i]))
