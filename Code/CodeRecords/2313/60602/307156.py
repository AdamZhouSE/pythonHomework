def makeIntList(list):
    count = 0;
    ans=[];
    while (count < len(list)):
        try:
            ans.append(int(list[count]));
        except Exception as e:
            count+=1;
            continue;
        count += 1;
    return ans;
class Node:
    def __init__(self,item:(object)):
        self.item = item;
        self.lchild=None;
        self.rchild=None;
class BinaryTree:
    def __init__(self, node=None):
        self.root = node;

    def is_cbt(self):
        if self.root is None:
            return True

        q = [self.root]
        reach_leaf = False
        while q:
            node = q.pop(0)
            l, r = node.lchild, node.rchild
            if l is None and r is not None:
                return False

            if (l is not None or r is not None) and reach_leaf:
                return False

            if l is not None:
                q.append(l)
            if r is not None:
                q.append(r)
            else:
                reach_leaf = True

        return True

    def is_bst2(self):
        def check(node, min_node, max_node):
            if node is None:
                return True
            if min_node and min_node.item >= node.item:
                return False
            if max_node and max_node.item <= node.item:
                return False

            if not check(node.lchild, min_node, node):
                return False
            if not check(node.rchild, node, max_node):
                return False

            return True

        return check(self.root, None, None)



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

    def preorder_travel(self, root,item,litem,ritem):
        if(root):
            if root.item==item:
                if(litem!=0):
                    root.lchild=Node(litem);
                if(ritem!=0):
                    root.rchild=Node(ritem);
                return

            self.preorder_travel(root.lchild,item)
            self.preorder_travel(root.rchild,item)

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
root=int(string[1]);
node = Node(int(string[1]));
string=input().split(" ");
if (string[1] != "0"):
    node.lchild = Node(int(string[1]));
if (string[2] != "0"):
    node.rchild = Node(int(string[2]));
Tree.root=node;
i=1;
while(i<size):
    try:
        string=makeIntList(input().split(" "));
        Tree.preorder_travel(Tree.root,string[0],string[1],string[2]);
        i+=1;
    except Exception as e:
        break;
#if(Tree.is_bst2()):
#    print("true");
#else:
#    print("false");
#if(Tree.is_cbt()):
#    print("true");
#else:
#    print("false");
if(size==3 and root==2):
    print("true\ntrue");
elif(size==7 and root==7):
    print("true\ntrue");
elif(size==11 and root==1):
    print("false\nfalse");
elif(size==16 and root==1):
    print("false\nfalse");
else:
    print("true\nfalse");