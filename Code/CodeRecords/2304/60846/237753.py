class TNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

from collections import deque

def zigzagLevelOrder(root):
    levels = []
    if not root:
        return levels
    level = 0
    queue = deque([root, ])
    while queue:
        levels.append([])
        lens = len(queue)
        for i in range(lens):
            node = queue.popleft()
            if level % 2 == 0:
                levels[level].append(node.val)
            else:
                levels[level].insert(0, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root:
        return levels

    level = 0
    queue = deque([root, ])
    while queue:
        # start the current level
        levels.append([])
        # number of elements in the current level
        level_length = len(queue)

        for i in range(level_length):
            node = queue.popleft()
            # fulfill the current level
            levels[level].append(node.val)

            # add child nodes of the current level
            # in the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # go to next level
        level += 1

    return levels

def printLevelOrder(levels,flag):
    location = ['left', 'right']
    for idx,level in enumerate(levels):
        if flag:
            print('Level {} from {} to {}:'.format(idx + 1, location[idx % 2], location[(idx + 1) % 2]), end='')
        else:
            print('Level {} :'.format(idx+1),end='')
        for node in level:
            print('',node,end='')
      #  if not flag or idx!=len(levels)-1:
        print()

line=[int(x) for x in input().split()]
n=line[0]
rootIdx=line[1]
tree=[]
for i in range(n):
    tree.append([int(x) for x in input().split()])
treeNode={0:None}
for i in range(n):
    val=tree[i][0]
    treeNode[val]=TNode(val)
for i in range(n):
    curr=treeNode.get(tree[i][0])
    curr.left=treeNode.get(tree[i][1])
    curr.right=treeNode.get(tree[i][2])

root=treeNode.get(rootIdx)
printLevelOrder(levelOrder(root),False)
printLevelOrder(zigzagLevelOrder(root),True)


# 8 1
# 2 4 0
# 4 0 0
# 3 5 6
# 5 7 8
# 6 0 0
# 7 0 0
# 8 0 0
# 1 2 3