class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
  
  
class BTree():
    def __init__(self, root=None):
        self.root = root
  
    # 根据先序、中序建树
    def construct_tree_pm(self, pre_order, mid_order):
        # 忽略参数合法性判断
        if len(pre_order) == 0:
            return None
        # 前序遍历的第一个结点一定是根结点
        root_data = pre_order[0]
        i = mid_order.index(root_data)
        # 递归构造左子树和右子树
        left = self.construct_tree_pm(pre_order[1: 1 + i], mid_order[:i])
        right = self.construct_tree_pm(pre_order[1 + i:], mid_order[i + 1:])
        return TNode(root_data, left, right)
  
  
    # 后序遍历
    def post_order(self, root):
        if root == None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data,end='')
  
 
sa = []
s = str(input())
while True or s!='':
    try:
        sa.append(s)
        s = input()      
    except EOFError:
        break;       
for i in range(0, len(sa), 2):
    po = sa[i]
    mo = sa[i + 1]   
    tree = BTree()
    root = tree.construct_tree_pm(po, mo)
    tree.post_order(root)
    print()