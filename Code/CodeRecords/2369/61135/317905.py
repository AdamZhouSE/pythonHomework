class Node:
    def __init__(self,item:(object)):
        self.item = item
        self.lchild=None
        self.rchild=None
class BinaryTree:
    def __init__(self,node=None):
        self.root=node
    def breadh_travel(self,item,litem,ritem):
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            if(node.item==item):
                if (litem != "*"):
                    node.lchild = Node(litem);
                if (ritem != "*"):
                    node.rchild = Node(ritem);
                return;
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
    def preorder_travel(self,root):
        if root:
            print(root.item, end="")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)
Tree=BinaryTree()
size=int(input())
string = input()
node = Node(string[0])
if (string[1] != "*"):
    node.lchild = Node(string[1])
if (string[2] != "*"):
    node.rchild = Node(string[2])
Tree.root=node
i=1
while(i<size):
    string=input()
    Tree.breadh_travel(string[0],string[1],string[2])
    i+=1
Tree.preorder_travel(Tree.root)