import sys
import re
import math
import copy
class Node():
    def __init__(self,data=None,left=None,right=None,val=None):
        self.data=data
        self.right=right
        self.left=left
        self.val=val
class Bintree():
    def __init__(self):
        self.root=None
        self.ls=[]
        self.max_value = 0
    def father_son_insert(self,root,left,right):
        '''root 是要插入的父节点'''
        curr=self.search_node(self.root,root.data)
        if left.data!=0:
            curr.left=left
        if right.data!=0:
            curr.right=right
    def father_son_insert_val(self,root,left,right,val):
        '''root 是要插入的父节点'''
        curr=self.search_node(self.root,root.data)
        if left.data!=0:
            curr.left=left
        if right.data!=0:
            curr.right=right
        curr.val=val
    def single_insert(self,root,item):
        curr=self.search_node(self.root,root.data)
        if item.data!=0:
            if curr.left is None:
                curr.left=item
            else:
                curr.right=item

    def binsearch_insert(self,item,root):
        if self.root is None:
            self.root=item
            return
        if root is None:
            root=item
        else:
            if item.data<=root.data:
                root.left=self.binsearch_insert(item,root.left)
            else:
                root.right=self.binsearch_insert(item,root.right)
        return root
    def binsearch_judge(self,node):
        global lastvalue
        lastvalue=0  #遍历的前一个节点的值
        def isbst2(node):
            global lastvalue
            if node==None:
                return True
            if isbst2(node.left) is not True:
                return False
            if node.data<lastvalue:
                return False
            lastvalue=node.data#更新
            if isbst2(node.right) is not True:
                return False
            return True
        return isbst2(node)
    def level_insert(self,item):
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
    def search_node(self,root,data):
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
    def x_level_print(self,root,level):
        '''打印某一层'''
        if root is None:
            return
        if level==1:
            print(root.data,end=' ')
        else:
            self.print_level(root.left,level-1)
            self.print_level(root.right,level-1)
    def all_level_print(self, pRoot):
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
    def get_node_numbers(self,root):
        global nums
        nums=0
        def count(root):
            global nums
            if root is None:
                return nums
            nums+=1
            count(root.left)
            count(root.right)
            return nums

        return count(root)

def son(arr1):
    cons1=[]
    for i in range(len(arr1)):
        for k in range(i, len(arr1)):
            cons1.append(arr1[i:k + 1])
    return cons1
if __name__=='__main__':
    want=input().split(' ')
    n=int(want[0])
    tree=Bintree()
    tree.root=Node(int(want[1]))
    for i in range(n):
        temp=input().split(' ')
        temp=[int(x) for x in temp]
        temproot=Node(temp[0])
        templeft=Node(temp[1])
        tempright=Node(temp[2])
        tree.father_son_insert(temproot,templeft,tempright)
    cons=[]
    for i in tree.levelorder(tree.root):
        node=tree.search_node(tree.root,i)
        if tree.binsearch_judge(node):
            cons.append(tree.get_node_numbers(node))
    con=max(cons)
    if (con==1):
        con=3
        
    print(con)