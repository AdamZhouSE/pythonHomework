min=10000
shu=0
class Node1(object):
    def __init__(self, key=None, left=None, right=None):
        self.key = key    # 数据域
        self.left = left    # 左子树
        self.right = right  # 右子树

def digui(list1,list2,Node):
    if len(list1)==1:
        Node.key=list1[0]
    elif len(list1)==0:
        a=1
    else:
        Node.left=Node1(0)
        Node.right=Node1(0)
        root=list2[len(list2)-1]
        Node.key=root
        weizhi =0
        for i in range(0,len(list1)):
            if list1[i]==root:
                weizhi=i
                break
        digui(list1[0:weizhi],list2[0:weizhi],Node.left)
        digui(list1[weizhi+1:len(list1)],list2[weizhi:len(list2)-1],Node.right)

def digui1(Node,he):
    global min
    global shu
    he=he+Node.key
    if Node.right!=None :
        if Node.right.key!=0:
            digui1(Node.right,he)
    if Node.left!=None :
        if Node.left.key!=0:
            digui1(Node.left,he)
    if((Node.right==None or Node.right.key==0) and (Node.left==None or Node.left==0) ):
        if min>he:
            min = he
            shu = Node.key

if __name__ == "__main__":
    zhongxu=input().split(' ')
    houxu=input().split(' ')
    for i in range(0,len(zhongxu)):
        zhongxu[i]=int(zhongxu[i])
        houxu[i]=int(houxu[i])
    root1=Node1(0)
    digui(zhongxu,houxu,root1)
    digui1(root1,0)
    print(shu)