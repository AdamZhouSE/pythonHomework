sum=0
max=0
class tree(object):
    def __init__(self, key=None,zi=None ,left=None, right=None):
        self.key = key    # 数据域
        self.zi=zi
        self.left = left    # 左子树
        self.right = right  # 右子树

    def goujian(self,key):
        self.key=key
        for i in range(0,len(list)):
            if list[i][0]==self.key:
                self.zi=list[i][3]
                if list[i][1]!=0:
                    self.left=tree(list[i][1])
                    tree.goujian(self.left,list[i][1])
                if list[i][2]!=0:
                    self.right=tree(list[i][2])
                    tree.goujian(self.right,list[i][2])
    def chazhao(self,he,count):
        global max
        if he+self.zi==sum:
            if count>max:
                max=count
        if self.left!=None:
            tree.chazhao(self.left,he+self.zi,count+1)
            tree.chazhao(self.left,0,1)
        if self.right!=None:
            tree.chazhao(self.right,he+self.zi,count+1)
            tree.chazhao(self.right,0,1)
a=input().split(' ')
root=tree(int(a[1]))
list=[]
for i in range(0,int(a[0])):
    b=input().split(' ')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
sum=int(input())
tree.goujian(root,root.key)
tree.chazhao(root,0,1)
print(max)