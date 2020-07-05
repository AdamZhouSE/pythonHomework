class Node:
    def __init__(self,item:(object)):
        self.item = item;
        self.lchild=None;
        self.rchild=None;


class BinaryTree:
    def __init__(self,node=None):
        self.root=node;

    def breadh_travel(self,item,litem,ritem):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop(0)
            # print(node.item, end=" ")
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

    def add(self, item):
        """
        广度优先遍历方式添加结点
        :param item:
        :return:
        """
        if self.root is None:
            self.root = Node(item)
        else:
            queue = []
            queue.append(self.root)

            while len(queue) > 0:
                node = queue.pop(0)
                if not node.lchild:
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(node.rchild)


    def preorder_travel(self, root):
        if root:
            print(root.item, end="")
            self.preorder_travel(root.lchild)
            self.preorder_travel(root.rchild)

    def inorder_travel(self, root):
        if root:
            self.inorder_travel(root.lchild)
            print(root.item, end="")
            self.inorder_travel(root.rchild)
    def postorder_travel(self, root):
        if root:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end="")

Tree=BinaryTree();
size=int(input());
string = input();
node = Node(string[0]);
if (string[1] != "*"):
    node.lchild = Node(string[1]);
if (string[2] != "*"):
    node.rchild = Node(string[2]);
Tree.root=node;
i=1;
while(i<size):
    string=input();
    Tree.breadh_travel(string[0],string[1],string[2]);
    i+=1;
Tree.preorder_travel(Tree.root);
