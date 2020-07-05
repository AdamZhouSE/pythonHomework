import sys
import re
import math
import copy
class Node():
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left
class Bintree():
    def __init__(self):
        self.root=None
        self.ls=[]
        self.max_value = 0
    def insert(self,root,left,right):
        '''root 是要插入的父节点'''
        curr=self.levelordersearch(self.root,root.data)
        if left.data!=0:
            curr.left=left
        if right.data!=0:
            curr.right=right
    def single_insert(self,root,item):
        curr=self.levelordersearch(self.root,root.data)
        if item.data!=0:
            if curr.left is None:
                curr.left=item
            else:
                curr.right=item

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
        return result
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
        '''打印每一层 int【int【】】'''
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
        '''前序中序建立二叉树'''
        if midlist:
            ind=midlist.index(prelist.pop(0))
            node=Node(midlist[ind])
            if self.root is None:
                self.root=node
            node.left=self.pre_mid_add(prelist,midlist[0:ind])
            node.right=self.pre_mid_add(prelist,midlist[ind+1:])
            return node

    def mid_post_add(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 思路：根据后序找到根节点，根据中序对左右子树进行区分
        if len(inorder) == 0 or len(postorder) == 0:
            return
        else:
            root = Node(postorder[-1])
            index_ = inorder.index(root.data)
            if self.root is None:
                self.root=root
            left_inorder, left_postorder = inorder[:index_], postorder[:index_]
            right_inorder, right_postorder = inorder[index_ + 1:], postorder[index_:-1]
            root.left = self.mid_post_add(left_inorder, left_postorder)
            root.right = self.mid_post_add(right_inorder, right_postorder)
            return root

    def max_sum(self, root, Sum):
        '''求最大路径 return int'''
        if root == None:
            return (self.max_value)
        if (root.left != None) & (root.right != None):
            self.max_sum(root.left, Sum + root.data)
            self.max_sum(root.right, Sum + root.data)
        elif (root.left != None) & (root.right == None):
            self.max_sum(root.left, Sum + root.data)
        elif (root.left == None) & (root.right != None):
            self.max_sum(root.right, Sum + root.data)
        else:
            if (Sum + root.data) > self.max_value:
                self.max_value = Sum + root.data

    def dfs(self,node, result, tmp=list()):
        '''求路径 return list'''
        if node is None:
            return
        tmp.append(node)
        # 这里需要用拷贝而不是用 = 赋值，也可以遍历赋值
        tmp1 = tmp.copy()

        if node.left is None and node.right is None:
            result.append([i.data for i in tmp])
            return

        if node.left is not None:
            self.dfs(node.left, result, tmp)
        # 遍历右子树需要带上不同的变量，否则左子树的tmp和右子树的tmp都指向一块内存
        if node.right is not None:
            self.dfs(node.right, result, tmp1)

    def minPathSum(self,node):
        '''求最小路径 return int'''
        if not node:
            return 0
        if node.left and node.right:
            return min(self.minPathSum(node.left), self.minPathSum(node.right)) + node.data
        elif node.left:
            return self.minPathSum(node.left) + node.data
        elif node.right:
            return self.minPathSum(node.right) + node.data
        else:
            return node.data
if __name__=='__main__':
    want=input().split(' ')
    N=int(want[0])
    root=Node(int(want[1]))
    tree=Bintree()
    tree.root=root
    for i in range(N):
        temp=input().split(' ')
        temproot=Node(int(temp[0]))
        templeft=Node(int(temp[1]))
        tempright=Node(int(temp[2]))
        tree.insert(temproot,templeft,tempright)
    r=[]
    tree.dfs(tree.root,result=r)
    M=int(input())
    tar=[]
    all=[]
    for i in range(M):

        temp=input().split(' ')
        temp=[int(x) for x in temp]
        all.append(temp)
    for temp in all:
        route=[]
        for k in r:
            if k.count(temp[0])!=0 and k.count(temp[1])!=0:
                route=[k]
                break
            if k.count(temp[0])!=0 or k.count(temp[1])!=0:
                route.append(k)
        if len(route)==1:
            tar.append(route[0][min(route[0].index(temp[0]),route[0].index(temp[1]))])
        else:
            '''temp0 在route1里'''
            if route[0].count(temp[0])==0:
                index1=route[1].index(temp[0])-1
                index2 = route[1].index(temp[1])-1
                while index1>=0:
                    index2 = route[1].index(temp[1]) - 1
                    mark=1
                    while index2>=0:
                        if route[1][index1]==route[0][index2]:
                            tar.append(route[1][index1])
                            mark=0
                            break
                        index2-=1
                    if mark==0:
                        break
                    index1-=1

            else:
                index2 = route[1].index(temp[1])-1
                index1 = route[0].index(temp[0])-1
                while index1>=0:
                    mark=1
                    index2 = route[1].index(temp[1]) - 1
                    while index2>=0:
                        if route[0][index1]==route[1][index2]:
                            tar.append(route[0][index1])
                            mark=0
                            break
                        index2-=1
                    if mark==0:
                        break
                    index1-=1
    for i in tar:
        print(i)








