class node():
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right
n = int(input())
nums = list(map(int, input().split()))
def solve(tree, num):
    if tree == None:
        print(-1)
        return node(num, None, None)
    if num < tree.val:
        if tree.left == None:
            tree.left = node(num, None, None)
            print(tree.val)
            return tree
        else:
            tree.left = solve(tree.left, num)
    elif num > tree.val:
        if tree.right == None:
            tree.right = node(num, None, None)
            print(tree.val)
            return tree
        else:
            tree.right = solve(tree.right, num)
    return tree
root = None
for x in nums:
    root = solve(root, x)
