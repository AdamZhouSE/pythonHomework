xianxu=[]
zhongxu=[]
houxu=[]
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

    def xianxu(self):
        xianxu.append(self.key)
        if self.left!=None:
            tree.xianxu(self.left)
        if self.right!=None:
            tree.xianxu(self.right)

    def zhongxu(self):
        if(self.left!=None):
            tree.zhongxu(self.left)
        zhongxu.append(self.key)
        if(self.right!=None):
            tree.zhongxu(self.right)


    def houxu(self):
        if(self.left!=None):
            tree.houxu(self.left)
        if (self.right != None):
            tree.houxu(self.right)
        houxu.append(self.key)


a=input().split(' ')
root=int(a[1])
list=[]
a=int(a[0])
for i in range(0,a):
    a=input().split()
    for j in range(0,3):
        a[j]=int(a[j])
    list.append(a)
root=tree(root)
tree.goujian(root,root.key)
tree.xianxu(root)
print(" ".join(str(i) for i in xianxu),end=" ")
print()
tree.zhongxu(root)
tree.houxu(root)
print(" ".join(str(i) for i in zhongxu),end=" ")
print()
print(" ".join(str(i) for i in houxu))