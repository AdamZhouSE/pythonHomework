class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
 
class Tree(object):
    def __init__(self):
         self.root = None

    def construct_tree(self, values=None):
        if not values:
             return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
                
root = Tree()
s = input()
if s.find('null'):
    nr = s.replace('null', 'None')
root.construct_tree(nr)


depth = 1
queue = [root, ]
while queue:
    lens = len(queue)
for i in range(lens):
    p = queue.pop(0)
    if p.left is None and p.right is None:
        print(depth)
    if p.left:
        queue.append(p.left)
    if p.right:
        queue.append(p.right)
depth += 1
print(depth)

