class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
class Bintree():
    def __init__(self):
        self.root=None
        self.ls=[]
    def insert(self,root,left,right):
        curr=self.levelordersearch(self.root,root.data)
        if left.data!=0:
            curr.left=left
        if right.data!=0:
            curr.right=right
    def leveladd(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
            self.ls.append(self.root)
        else:
            rootNode=self.ls[0]
            if rootNode.left==None:
                rootNode.left=node
                self.ls.append(rootNode.left)

            elif rootNode.right==None:
                rootNode.right=node
                self.ls.append(rootNode.right)
                self.ls.pop(0)
    def find(self,node,key):
        if node is None:
            return None
        if node.data==key:
            return node
        if node.data>key:
            return self.find(node.left,key)
        else:
            return self.find(node.right,key)
    def preorder(self,root):
        '''前序遍历'''
        if root is None:
            return
        print(root.data,end='')
        self.preorder(root.left)
        self.preorder(root.right)
    def pre_order_stack(self, root):  # 堆栈实现前序遍历（非递归）
        if not root:
            return
        myStack = []
        node = root
        cons=[]
        while myStack or node:
            while node:  # 从根节点开始，一直寻找他的左子树
                cons.append(node.data)
                myStack.append(node)
                node = node.left
            node = myStack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right  # 开始查看它的右子树
        return cons
    def inorder(self, root):
        '''中序遍历'''
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=' ')
        self.inorder(root.right)
    def in_order_stack(self, root):  # 堆栈实现中序遍历（非递归）
        if not root:
                return
        cons=[]
        myStack = []
        node = root
        while myStack or node:  # 从根节点开始，一直寻找它的左子树
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            cons.append(node.data)
            node = node.right
        return cons
    def postorder(self, root):
        '''后序遍历'''
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=' ')
    def post_order_stack(self, root):  # 堆栈实现后序遍历（非递归）
        # 先遍历根节点，再遍历右子树，最后是左子树，这样就可以转化为和先序遍历一个类型了，最后只把遍历结果逆序输出就OK了。
        if not root:
            return
        myStack1 = []
        myStack2 = []
        node = root
        cons=[]
        while myStack1 or node:
            while node:
                myStack2.append(node)
                myStack1.append(node)
                node = node.right
            node = myStack1.pop()
            node = node.left
        while myStack2:
            cons.append(myStack2.pop().data)
        return  cons
    def levelorder(self,root):
        '''层序遍历'''
        if root is None:
            return
        queue=[]
        result=[]
        node=root
        queue.append(root)
        while queue:
            node=queue.pop(0)
            result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print(result)
    def levelordersearch(self,root,data):
        '''层序遍历'''
        if root is None:
            return
        queue=[]
        result=[]
        node=root
        queue.append(root)
        while queue:
            node=queue.pop(0)
            if node.data==data:
                return node
            result.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return None
    def depth(self,root):
        '''层序遍历'''
        if root is None:
            return 0
        lDepth=self.depth(root.left)
        rDepth=self.depth(root.right)
        return max(lDepth,rDepth)+1
    def LChild_Of_Node(self,node):
        return node.left if node.left is not None else None
    def RChild_Of_Node(self,node):
        return node.right if node.right is not None else None
    def print_level(self,root,level):
        '''打印某一层'''
        if root is None:
            return
        if level==1:
            print(root.data,end=' ')
        else:
            self.print_level(root.left,level-1)
            self.print_level(root.right,level-1)
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        queue=[pRoot]
        outList=[]
        while queue:
            res=[]
            nextQueue=[]
            for point in queue:     #这里再遍历每一层
                res.append(point.data)
                if point.left:
                    nextQueue.append(point.left)
                if point.right:
                    nextQueue.append(point.right)
            outList.append(res)
            queue=nextQueue     #这一步很巧妙，用当前层覆盖上一层
        return outList


if __name__=='__main__':
    inf=input().split(' ')
    allnodenum=int(inf[0])
    treeroot=Node(int(inf[1]))
    tree=Bintree()
    tree.root=treeroot
    for i in range(allnodenum):
        arr=input().split(' ')
        temproot=Node(int(arr[0]))
        templeft=Node(int(arr[1]))
        tempright=Node(int(arr[2]))
        tree.insert(temproot,templeft,tempright)
    dep=tree.depth(tree.root)
    alllevel=tree.Print(tree.root)
    for i in range(dep):
        temp=' '.join(str(x) for x in alllevel[i])
        print('Level '+str(i+1)+' : '+temp)
    for i in range(dep):
        temp = ' '.join(str(x) for x in alllevel[i])
        if i%2==0:
            print('Level '+str(i+1)+' from left to right: '+temp)
        else:
            alllevel[i].reverse()
            temp = ' '.join(str(x) for x in alllevel[i])
            print('Level '+str(i+1)+' from right to left: '+temp)
