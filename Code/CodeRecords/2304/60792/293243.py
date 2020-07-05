class TreeNode:
    def _init_(self,x):
        self.val=x
        self.lelf=None
        self.right=None

class BinaryTree:
    def _init_(self):
        self.root=None
    def make_tree(self,node):
        self.root=node
    def insert(self, node):
        # 这里是建立一个完全二叉树
        lst = []
        def insert_node(tree_node, p, node):
            if tree_node._left is None:
                tree_node._left = node
                lst.append(tree_node._left)
                return
            elif tree_node._right is None:
                tree_node._right = node
                lst.append(tree_node._right)
                return
            else:
                lst.append(tree_node._left)
                lst.append(tree_node._right)
                if p > (len(lst) -2):
                    return
                else:
                    insert_node(lst[p+1], p+1, node)
        lst.append(self.root)
        insert_node(self.root, 0, node)
        
        
n,m=map(int,input().split())
for i in range(0,n):
    a,b,c=map(int,input().split(" "))
    if a==m:
        node=TreeNode(m)
        tree=BinaryTree()
        tree.make_tree(node)
    else:
        
    
    
    
    
    