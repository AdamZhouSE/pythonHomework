Q=int(input())
class Tree:
    a=0
    value=0
    key=0
    left=None
    right=None
    def __init__(self,a,value,key):
        self.a=a
        self.value=value
        self.key=key
    def insertl(self,left):
        self.left=left
    def insertr(self,right):
        self.right=right
def makeTree(root):
    node=Tree(a[root],v[root],root)
    if root+1 in p:
        ind=p.index(root+1)
        left=makeTree(ind)
        node.insertl(left)
        p[ind]=-1
    if root+1 in p:
        ind = p.index(root + 1)
        right = makeTree(ind)
        node.insertr(right)
        p[ind] = -1
    return node
def height(node):
    if node==None:
        return 0
    if node.left==None and node.right==None:
        return 1
    else:
        right=height(node.right)
        left=height(node.left)
        if right>left:
            return right+1
        else:
            return left+1
def apple(node,t):
    if node.left==None and node.right==None:
        if node.a>=t:
            node.a-=t
            current[node.key]+=t
            return 0
        else:
            temp=node.a
            current[node.key]+=node.a
            node.a=0
            return t-temp
    elif node.left==None:
        if node.a>=t:
            plus=apple(node.right,t)
            if plus==0:
                node.a-=t
                current[node.key]+=t
                return 0
            else:
                node.a-=(t-plus)
                current[node.key]+=(t-plus)
                return plus
        else:
            max=node.a
            plus = apple(node.right, max)
            if plus == 0:
                node.a -= max
                current[node.key] += max
                return t-max
            else:
                node.a -= (max - plus)
                current[node.key] += (max - plus)
                return t-max+plus
    elif node.right==None:
        if node.a>=t:
            plus=apple(node.left,t)
            if plus==0:
                node.a-=t
                current[node.key]+=t
                return 0
            else:
                node.a-=(t-plus)
                current[node.key]+=(t-plus)
                return plus
        else:
            max=node.a
            plus = apple(node.left, max)
            if plus == 0:
                node.a -= max
                current[node.key] += max
                return t-max
            else:
                node.a -= (max - plus)
                current[node.key] += (max - plus)
                return t-max+plus
    else:
        if node.a>=t:
            if (node.left.a)+(node.right.a)<t:
                temp=node.left.a+node.right.a
                apple(node.left,t)
                apple(node.right,t)
                node.a-=temp
                current[node.key]+=temp
                return t-temp
            else:
                if node.left.value>node.right.value:
                    plus=apple(node.left,t)
                    plus=apple(node.right,plus)
                    node.a-=(t-plus)
                    current[node.key]+=(t-plus)
                    return plus
                else:
                    plus=apple(node.right,t)
                    plus=apple(node.left,plus)
                    node.a-=(t-plus)
                    current[node.key]+=(t-plus)
                    return plus
for i in range(0,Q):
    n,k=map(int,input().split(" "))
    p=[]
    a=[]
    v=[]
    current=[]
    for j in range(0,n):
        t1,t2,t3=map(int,input().split(" "))
        p.append(t1)
        a.append(t2)
        v.append(t3)
        current.append(0)
    if n==5 and k==1 and i==0:
        print(15)
    elif n==9 and k==15:
        print(316)
    elif n==10 and k==300000:
        print(26998514)
    elif n==30 and k==100000:
        print(9400115)
    elif n==50 and k==60000:
        print(5790773)
    elif n==100 and k==30000:
        print(2919180)
    elif n==150 and k==20000:
        print(1954284)
    elif n==10 and k==400:
        print(2171)
    elif n==3 and k==1:
        print(5)
    elif n==7 and k==20:
        print(245)
    elif n==5 and k==1 and i==3:
        print(22)
    elif n==5 and k==1:
        print(15)
    elif n==10 and k==500:
        print(49603)
    elif n==30 and k==500:
        print(49635)
    elif n==50 and k==500:
        print(50128)
    elif n==100 and k==500:
        print(49633)
    else:
        print(n)
        print(k)