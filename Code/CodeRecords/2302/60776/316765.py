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
        for i in range(0,len(list)):
            if list[i][0]==self.key:
                if list[i][1] != 0:
                    self.left = tree(list[i][1])
                    tree.goujian(self.left, list[i][1])
                if list[i][2] != 0:
                    self.right = tree(list[i][2])
                    tree.goujian(self.right, list[i][2])

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

a=input().split(' ')
root=tree(int(a[1]))
list=[]
for  i in range(0,int(a[0])):
    b=input().split(' ')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
tree.goujian(root,root.key)
a=int(input())
for i in range(0,a):
    a=input().split(' ')
    jiedian1=int(a[0])
    jiedian2=int(a[1])
    tree.bianli(root,jiedian1,[1])
    tree.bianli(root,jiedian2,[1])
    isfind=0
    for j in range(len(bianli1)-1,-1,-1):
        for m in range(len(bianli2)-1,-1,-1):
            if bianli1[j]==bianli2[m]:
                print(bianli1[j])
                isfind=1
                break
        if isfind==1:
            break
    count1=0
    bianli1.clear()
    bianli2.clear()