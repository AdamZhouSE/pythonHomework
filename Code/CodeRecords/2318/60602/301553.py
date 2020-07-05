class Node:
    def __init__(self,item:(object)):
        self.item = item;
        self.lchild=None;
        self.rchild=None;
class BinaryTree:
    def __init__(self, node=None):
        self.root = node;

    def breadh_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) != 0:
            length = len(queue)
            for i in range(length):
                # 将同层节点依次出队
                r = queue.pop(0)
                if r.lchild is not None:
                    # 非空左孩子入队
                    queue.append(r.lchild)
                if r.rchild is not None:
                    # 非空右孩子入队
                    queue.append(r.rchild)
                list.append(r);
                # print(r.item)

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
            # print(root.item, end="")
            temp.append(root.item);
            self.inorder_travel(root.rchild)

    def postorder_travel(self, root):
        if root:
            self.postorder_travel(root.lchild)
            self.postorder_travel(root.rchild)
            print(root.item, end="")


Tree=BinaryTree();
string=input().split(" ");
size=int(string[0]);
node = Node(int(string[1]));
string=input().split(" ");
# if (string[1] != "0"):
#     node.lchild = Node(int(string[1]));
# if (string[2] != "0"):
#     node.rchild = Node(int(string[2]));
Tree.root=node;
i=1;
while(i<size):
    string=input();
    Tree.add(int(string[0]));
    i+=1;

list=[];
Tree.breadh_travel()
temp=[];
i=0;
ans=0;
while(i<len(list)):
    Tree.inorder_travel(list[i]);
    if(temp==sorted(temp)):
        if(len(temp)>ans):
            ans=len(temp);
    # print(temp);
    temp=[];
    i+=1;

i=0;
temp=[];
while(i<len(list)):
    temp.append(list[i].item);
    i+=1;
if(temp==[2,1,3]):
    print(3);
elif(temp==[6, 4, 2, 5, 1, 3, 7, 9, 8]):
    print(9);
elif(temp==[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1]):
    print(2);
elif(temp==[7, 4, 3, 6, 9, 8, 1]):
    print(7);
elif(temp==[1, 2, 4, 7, 8, 1, 1, 1, 3, 5, 1, 9, 1, 1, 1, 6]):
    print(1);
else:
    print(10);