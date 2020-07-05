class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def minDepth(self, root):

    if not root:
        return 0

    children = [root.left, root.right]
    # if we're at leaf node
    if not any(children):
        return 1

    min_depth = float('inf')
    for c in children:
        if c:
            min_depth = min(self.minDepth(c), min_depth)
    return min_depth + 1

inp=input()
nums=inp[1:-1].split(",")
for i in range(len(nums)):
    if(nums[i]!="null"):
        nums[i]=int(nums[i])
print(minDepth(nums))


