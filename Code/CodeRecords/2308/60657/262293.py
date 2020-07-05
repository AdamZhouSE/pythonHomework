import sys
import re
import math
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
        print(root.data,end=' ')
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
        print(root.data,end='')
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

    def pre_mid_add(self,prelist,midlist):

        if midlist:
            ind=midlist.index(prelist.pop(0))
            node=Node(midlist[ind])
            if self.root is None:
                self.root=node
            node.left=self.pre_mid_add(prelist,midlist[0:ind])
            node.right=self.pre_mid_add(prelist,midlist[ind+1:])
            return node


if __name__=='__main__':
    arr=input().split(' ')
    n=int(arr[0])
    treeroot=Node(int(arr[1]))
    tree=Bintree()
    tree.root=treeroot
    for i in range(n):
        A=input().split(' ')
        temproot=Node(int(A[0]))
        templeft=Node(int(A[1]))
        tempright=Node(int(A[2]))
        tree.insert(temproot,templeft,tempright)
    tar=int(input())
    post=tree.in_order_stack(tree.root)
    if post.index(tar)!=len(post)-1:
        print(post[post.index(tar)+1])
    else:
        print(0)