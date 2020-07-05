houxu=[]
class tree(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

    def goujian(self,xian,zhong):
        if len(xian)!=0:
            self.key = xian[0]
            count = 0
            for i in range(0, len(zhong)):
                if zhong[i] == xian[0]:
                    count = i
                    break
            if len(xian[1:count+1])!=0:
                self.left=tree(xian[1])
                tree.goujian(self.left, xian[1:count + 1], zhong[0:count])
            if len(xian[count+1:])!=0:
                self.right=tree(xian[count+1])
                tree.goujian(self.right, xian[count + 1:], zhong[count + 1:])

    def houxu(self):
        if(self.left!=None):
            tree.houxu(self.left)
        if (self.right != None):
            tree.houxu(self.right)
        houxu.append(self.key)

for i in range(0,2):
    xian = input()
    zhong = input()
    root = tree(xian[0])
    tree.goujian(root, xian, zhong)
    tree.houxu(root)
    print("".join(houxu))
    houxu=[]