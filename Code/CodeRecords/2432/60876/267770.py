class Node:
    def __init__(self,keyword):
        self.key=keyword
        self.right=None
        self.left=None
        self.value=keyword
    def insertleft(self,node):
        self.left=node
    def insertright(self,node):
        self.right=node
    def getright(self):
        return self.right.key
    def getleft(self):
        return self.left.key
    def getroot(self):
        return self.key
mid=list(map(int,input().split(" ")))
after=list(map(int,input().split(" ")))
def create(nums1,nums2):
    len1=len(nums1)
    len2=len(nums2)
    if len1==0:
        return None
    root=Node(nums2[len2-1])
    if len1==1:
        return root
    ind=0
    while nums1[ind]!=nums2[len2-1]:
        ind+=1
    left1=nums1[0:ind]
    right1=nums1[ind+1:len1]
    lenl=len(left1)
    left2=nums2[0:lenl]
    right2=nums2[lenl:len2-1]
    left=create(left1,left2)
    right=create(right1,right2)
    root.insertleft(left)
    root.insertright(right)
    return root
def setvalue(root):
    if root==None:
        return
    else:
        if root.left!=None:
            root.left.value+=root.value
            setvalue(root.left)
        if root.right!=None:
            root.right.value+=root.value
            setvalue(root.right)
tree=create(mid,after)
setvalue(tree)
min=1000
ind=-1
def bianli(root,list):
    if root.left==None and root.right==None:
        if root.value<list[0]:
            list[0]=root.value
            list[1]=root.key
        elif root.value==list[0]:
            if root.key<list[1]:
                list[1]=root.key
        return list
    else:
        if root.left==None:
            return bianli(root.right,list)
        elif root.right==None:
            return bianli(root.left,list)
        else:
            left=bianli(root.left,list)
            right=bianli(root.right,list)
            if left[0]<right[0]:
                return left
            elif left[0]>right[0]:
                return right
            else:
                if left[1]>right[1]:
                    return right
                else:
                    return left
result=bianli(tree,[min,ind])
print(result[1])