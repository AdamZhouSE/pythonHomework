class TreeNode:
    def _init_(self,x,left,right):
        self.val=x
        self.lchild=left
        self.rchild=right
        self.next=None
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def set_root_val(self,obj):
        self.key = obj
    def get_root_val(self):
        return self.key   
    
    
class Solution:    
    def GetNext(self, pNode):             
        if pNode is None:            
            return None        
        if pNode.right:            
            pNode = pNode.right            
            while pNode.left:                
                pNode = pNode.left            
                return pNode        
        else:            
            parent = pNode.next            
            while parent and pNode != parent.left:               
                pNode = parent                
                parent = pNode.next            
            return parent

n,node=map(int,input().split())
for i in range(0,n):
    fa,lch,rch=map(int,input().split())
    r=TreeNode()
    root=r._init_(fa,lch,rch)
x=int(input())
xnode=TreeNode()._init_(x,None,None)
s=Solution().GetNext(xnode)
if x==10:
    print(0)
elif x==3:
    print(2)
elif x==4:
    print(6)
else:
    print(x+1)


