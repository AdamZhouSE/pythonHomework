list=[]
maxdepth=1
wide=1
bianli1=[]
bianli2=[]
count1=0
class tree(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

    def goujian(self,key):
        self.key=key
        count=0
        for i in range(0,len(list)):
            if list[i][0]==self.key:
                if count==0:
                    self.left = tree(list[i][1])
                    tree.goujian(self.left, list[i][1])
                    count+=1
                else:
                    self.right = tree(list[i][1])
                    tree.goujian(self.right, list[i][1])

    def shendu(self,depth):
        global maxdepth
        if self.left!=None:
            tree.shendu(self.left,depth+1)
        if self.right!=None:
            tree.shendu(self.right,depth+1)
        if depth>maxdepth:
            maxdepth=depth

    def kuandu(self,list):
        global wide
        if len(list)>wide:
            wide=len(list)
        list1=[]
        for i in range(0,len(list)):
            if list[i].left!=None:
                list1.append(list[i].left)
            if list[i].right!=None:
                list1.append(list[i].right)
        if list1!=[]:
            tree.kuandu(self, list1)

    def bianli(self,jiedian,list):
        global bianli1
        global bianli2
        global count1
        if self.key==jiedian:
            if count1==0:
                bianli1.extend(list)
                count1+=1
            else:
                bianli2.extend(list)
        else:
            if self.left!=None:
                temp=[]
                temp.extend(list)
                temp.append(self.left.key)
                tree.bianli(self.left,jiedian,temp)
            if self.right!=None:
                temp=[]
                temp.extend(list)
                temp.append(self.right.key)
                tree.bianli(self.right,jiedian,temp)

a=int(input())
for i in range(0,a-1):
    b=input().split(' ')
    while('' in b):
        b.remove('')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
root=tree(1)
tree.goujian(root,1)
tree.shendu(root,1)
tree.kuandu(root,[root])
a=input().split(' ')
print(maxdepth)
print(wide)
jiedian1=int(a[0])
jiedian2=int(a[1])
tree.bianli(root,jiedian1,[1])
tree.bianli(root,jiedian2,[1])
weizi1=0
weizi2=0
isright=0
for i in range(len(bianli1)-1,-1,-1):
    for j in range(len(bianli2)-1,-1,-1):
        if bianli1[i]==bianli2[j]:
            weizi1=i
            weizi2=j
            isright=1
            break
    if isright==1:
        break
print((len(bianli1)-1-weizi1)*2+(len(bianli2)-1-weizi2),end="")