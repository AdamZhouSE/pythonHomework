class Tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
        self.store_pre = []
        self.store_in =[]

    def Inorder(self,node):
        if self.root != None:
            if self.left != None:
                self.left.Inorder(node)
            node.store_in.append(self.root)
            if self.right != None:
                self.right.Inorder(node)
        else:
            return
    def Preorder(self,node):
        if self.root != None:
            node.store_pre.append(self.root)
            if self.left != None:
                self.left.Preorder(node)
            if self.right != None:
                self.right.Preorder(node)
        else:
            return
n  =int(input())
result_pre = []
result_in = []
for i in range(n+1):
    line = input()
    #初始化根节点
    temp = Tree(int(line[0]))
    line = line[1:]

    def search(node,element,pre,mode):
        if node == None:
            temp1 = Tree(element)
            if mode == "left":
                pre.left = temp1
            elif mode == "right":
                pre.right = temp1
        elif element<=node.root:
            search(node.left,element,node,"left")
        elif element>node.root:
            search(node.right,element,node,"right")
    for j in range(len(line)):
        search(temp,int(line[j]),temp,"")
    temp.Inorder(temp)
    result_in.append(temp.store_in)
    temp.Preorder(temp)
    result_pre.append(temp.store_pre)

for i in range(1,len(result_in)):
    if result_in[0] == result_in[i] and result_pre[0] == result_pre[i]:
        print("YES")
    else:
        print("NO")

