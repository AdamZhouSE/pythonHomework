class tree(object):
    def __init__(self, jiage=None, xuqiu=None,geshu=None,hangshu=None,ziji=None,left=None, right=None):
        self.ziji=ziji
        self.jiage = jiage
        self.xuqiu=xuqiu
        self.hangshu=hangshu
        self.geshu=geshu
        self.left = left
        self.right = right

    def goujian(self,jiage,xuqiu,geshu,hangshu,ziji):
        count=0
        self.ziji=ziji
        self.geshu=geshu
        self.hangshu=hangshu
        self.xuqiu=xuqiu
        self.jiage=jiage
        for i in range(0,len(list)):
            if list[i][0]==self.hangshu:
                if count==0:
                    self.left=tree(0)
                    tree.goujian(self.left,list[i][2],list[i][1],0,i+1,0)
                    count=1
                else:
                    self.right=tree(0)
                    tree.goujian(self.right,list[i][2],list[i][1],0,i+1,0)

    def goujian1(self):
        if self.left==None and self.right==None:
            self.geshu=self.xuqiu
            self.ziji=self.xuqiu
        else:
            if self.left!=None:
                self.geshu=self.geshu+self.left.geshu
            if self.right!=None:
                self.geshu=self.geshu+self.right.geshu

    def goujian2(self):
        if self.left != None:
            self.geshu = self.geshu + self.left.geshu
        if self.right != None:
            self.geshu = self.geshu + self.right.geshu
        self.geshu+=self.ziji

    def chazahzuixiao(self,min):
        if self.jiage<min:
            min=self.jiage
        if self.left!=None:
            min=tree.chazahzuixiao(self.left,min)
        if self.right!=None:
            min=tree.chazahzuixiao(self.right,min)
        return min

    def digui(self):
        if self.left!=None:
            tree.digui(self.left)
        if self.right!=None:
            tree.digui(self.right)
        tree.goujian2(self)
        if self.xuqiu>self.geshu:
            duoyu=self.xuqiu-self.geshu
            min=tree.chazahzuixiao(self,self.jiage)
            tree.zentian(self,min,duoyu)

    def zentian(self,min,duoyu):
        if self.jiage==min:
            self.ziji+=duoyu
            self.geshu+=duoyu
            return 0
        else:
            if self.left!=None:
                duoyu=tree.zentian(self.left,min,duoyu)
            if self.right!=None:
                duoyu=tree.zentian(self.right,min,duoyu)
            return duoyu
    def qiujie(self):
        result=0
        if self.left!=None:
            result+=tree.qiujie(self.left)
        if self.right!=None:
            result+=tree.qiujie(self.right)
        result+=self.ziji*self.jiage
        return result
a=int(input())
list=[]
for i in range(0,a):
    b=input().split(' ')
    b.remove('')
    for j in range(0,len(b)):
        b[j]=int(b[j])
    list.append(b)
root=tree(list[0][2],list[0][1],0,1,0)
tree.goujian(root,root.jiage,root.xuqiu,root.geshu,root.hangshu,root.ziji)
tree.goujian1(root)
tree.digui(root)
result=tree.qiujie(root)
print(result)