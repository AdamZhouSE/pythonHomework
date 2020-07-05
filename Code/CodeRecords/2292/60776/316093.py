max=0

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
    def jieguo(self,temp):
        global max
        temp+=1
        if self.left!=None:
            if self.left.key<self.key:
                temp=temp+tree.jieguo(self.left,0)
            else:
                tree.jieguo(self.left,0)
        if self.right!=None:
            if self.right.key>self.key:
                temp=temp+tree.jieguo(self.right,0)
            else:
                tree.jieguo(self.right,0)
        if temp>max:
            max=temp
        return temp

a=input().split(' ')
root=tree(int(a[1]))
list=[]
for i in range(0,int(a[0])):
    b=input().split(' ')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
tree.goujian(root,root.key)
tree.jieguo(root,0)
print(max)