class Node:
    def __init__(self,value,left,right,height):
        self.left = left
        self.right = right
        self.value = value
        self.height = height

#右单旋转,转前形式为最左边一条直线
def LLRotate(p:Node):
    #转
    tmp = p.left
    p.left = tmp.right
    tmp.right = p
    #调整tmp和p的高度
    p.height = max(get_height(p.left),get_height(p.left))+1
    tmp.height = max(get_height(tmp.left),get_height(tmp.right)) +1
    return tmp

#左单旋转，转前形式为最右边一条直线
def RRRotate(p:Node):
    tmp = p.right
    p.right = tmp.left
    tmp.left = p
    p.height = max(get_height(p.left),get_height(p.right)) +1
    tmp.height = max(get_height(tmp.right),get_height(tmp.left)) + 1
    return tmp

#先左后右双旋转，在失衡点的左孩子的右子树上插入
def LRRotate(p:Node):
    p.left = RRRotate(p.left)
    return LLRotate(p)

#先右后左双旋转，在失衡点的右孩子的左子树上插入
def RLRotate(p:Node):
    p.right = LLRotate(p.right)
    return RRRotate(p)

#获取节点的高度（从下往上）
def get_height(node:Node):
    if node == None:
        return -1
    else:
        return node.height

#插入
def insert(root:Node,data:int):
    if root == None:
        root = Node(data,None,None,0)
        return root
    #↓插在左树
    if data <= root.value:
        root.left = insert(root.left,data)
        #↓如果失衡
        if get_height(root.left) - get_height(root.right) == 2:
            if data <= root.left.value:#在左孩子的左边（树的外部）
                root = LLRotate(root)
            else:
                root = LRRotate(root)#在左孩子的右边（树的内部）
    #↓插在右树
    else:
        root.right = insert(root.right,data)
        #如果失衡↓
        if get_height(root.right) - get_height(root.left) == 2:
            if data <= root.right.value:
                root = RLRotate(root)
            else:
                root = RRRotate(root)
    root.height = max(get_height(root.left),get_height(root.right)) + 1
    return root

#删除
def remove(root:Node,data):
    if root == None:#没找到要删除的节点
        return None
    if data < root.value:#在左子树删除
        root.left = remove(root.left,data)
        if get_height(root.right) - get_height(root.left) == 2:
            if get_height(root.right.left) > get_height(root.right.right):
                root = RLRotate(root)
            else:
                root = RRRotate(root)
    elif data == root.value:#找到要删除的节点
        if root.left is not None and root.right is not None:#左右子树都非空
            root.value = get_suc(root).value
            root.right = remove(root.right,root.value)
        else:#只有左子树或只有右子树或为叶子节点
            root = root.right if root.left is None else root.left
    else:#在root的右子树上删除
        root.right = remove(root.right,data)
        if get_height(root.left) - get_height(root.right) == 2:
            if get_height(root.left.left) > get_height(root.left.right):
                root = LLRotate(root)
            else:
                root = LRRotate(root)
    #↓调整高度
    if root is not None:
        root.height = max(get_height(root.left),get_height(root.right)) + 1
    return root

#查询x数的排名。若有多个相同的数，因输出最小的排名
def get_rank(root:Node,data):
    if root is None:
        return 0
    if data < root.value:
        return get_rank(root.left,data)
    elif data == root.value:
        if root.left is not None and data == root.left.value:
            return get_rank(root.left,data)
        else:
            return get_rank(root.left,data) + 1
    elif data > root.value:
        return get_rank(root,root.value) + get_rank(root.right,data)

#查询排名为x的数
def get_num_by_rank(root:Node,aim,result:list,num):#初次调用result设为[],num为0
    if root.left is not None:
        num = get_num_by_rank(root.left,aim,result,num)
    result.append(root.value)
    if len(result) == aim:
        return result[-1]
    if root.right is not None:
        num = get_num_by_rank(root.right,aim,result,num)
    return num

#求x的前趋节点（不是前驱数值）
def get_pre(p:Node):
    if p is None:
        return None
    l = p.left
    while l is not None and l.right is not None:
        l = l.right
    return l

#求x的后继节点（不是后继数值）
def get_suc(p:Node):
    if p is None:
        return None
    r = p.right
    while r is not None and r.left is not None:
        r = r.left
    return r

#求前驱数值
def get_pre_num(num,root:Node,result:list,n):#list初次调用传[],n设0
    if root.left is not None:
        n = get_pre_num(num,root.left,result,n)

    result.append(root.value)
    if len(result) > 1 and result[-1] >= num and result[-2] < num:
        return result[-2]
    elif len(result) == 1 and result[0] < num:
        n = result[0]

    if root.right is not None:
        n = get_pre_num(num,root.right,result,n)
        
    if(result[-1]<num):
        return result[-1]
    return n

def get_suc_num(num,root:Node,result:list,n):#list初次调用传[],n传0
    if root.left is not None:
        n = get_suc_num(num, root.left, result,n)

    result.append(root.value)
    if len(result) > 1 and result[-1] > num and result[-2]<= num:
        return result[-1]
    elif len(result) == 1 and result[0] > num:
        n = result[0]
    if root.right is not None:
        n = get_suc_num(num, root.right, result,n)
    return n


T = int(input())
inpu1 = input().split(' ')
opt = int(inpu1[0])
x = int(inpu1[1])
root = Node(x,None,None,0)
for t in range(T-1):
    inpu1 = input().split(' ')
    opt = int(inpu1[0])
    x = int(inpu1[1])
    if opt == 1:
        root = insert(root,x)
    elif opt == 2:
        root = remove(root,x)
    elif opt == 3:
        print(get_rank(root,x))
    elif opt == 4:
        print(get_num_by_rank(root,x,[],0))
    elif opt == 5:
        print(get_pre_num(x,root,[],0))
    elif opt == 6:
        print(get_suc_num(x,root,[],0))


