
class tree(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

    def chazhao(self,zi):
        if zi>self.key:
            if self.right==None:
                print(self.key)
                self.right=tree(zi)
            else:
                tree.chazhao(self.right,zi)
        if zi<self.key:
            if self.left==None:
                print(self.key)
                self.left=tree(zi)
            else:
                tree.chazhao(self.left,zi)

a=int(input())
b=input().split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
root=tree(b[0])
print(-1)
for i in range(1,len(b)):
    tree.chazhao(root,b[i])