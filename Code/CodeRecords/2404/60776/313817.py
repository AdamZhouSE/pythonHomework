jiedianzi=[]
list=[]
he=0
result=0
jilu=[]
class tree(object):
    def __init__(self,zi=None, key=None, left=None, right=None,zhong=None):
        self.zi=zi
        self.key = key    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树
        self.zhong=zhong

    def goujian(self,zi,key):
        global list
        self.zi=zi
        self.key=key
        count=0
        for i in range(0,len(list)):
            if list[i][0]==self.key:
                if count == 0:
                    self.left = tree(jiedianzi[list[i][1]-1],list[i][1])
                    tree.goujian(self.left, jiedianzi[list[i][1]-1],list[i][1])
                    count=1
                elif count==1:
                    self.right = tree(jiedianzi[list[i][1]-1],list[i][1])
                    tree.goujian(self.right, jiedianzi[list[i][1]-1],list[i][1])
                    count+=1
                else:
                    self.zhong = tree(jiedianzi[list[i][1] - 1], list[i][1])
                    tree.goujian(self.zhong, jiedianzi[list[i][1] - 1], list[i][1])
    def qiuhe(self,temp):
        global result
        if temp+self.zi==he:
            result+=1
        if self.left!=None:
            tree.qiuhe(self.left,temp+self.zi)
        if self.right!=None:
            tree.qiuhe(self.right,temp+self.zi)
        if self.zhong!=None:
            tree.qiuhe(self.zhong,temp+self.zi)
        if temp!=0 and self.key not in jilu:
            jilu.append(self.key)
            tree.qiuhe(self,0)


a=input().split(' ')
he=int(a[1])
jiedianzi=input().split(' ')
for i in range(0,len(jiedianzi)):
    jiedianzi[i]=int(jiedianzi[i])
for i in range(0,int(a[0])-1):
    b=input().split(' ')
    if '' in b:
        b.remove('')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
root=tree(jiedianzi[0],1)
tree.goujian(root,root.zi,root.key)
tree.qiuhe(root,0)
print(result)
