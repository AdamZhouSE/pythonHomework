# coding = utf-8
class treeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.tag = 0 # 0 not tag
    def setTag(self,tag):
        self.tag = tag

def find(node,value):
    if(node == None):
        return None
    if(node.value == value):
        return node
    temp1 = find(node.left,value)
    temp2 = find(node.right,value)
    if(temp1 != None):
        return temp1
    elif(temp2 != None):
        return temp2
    else:
        return None

def find1(node,now,value):
    if(node == None):
        return None
    if(node.value == value):
        if(node.tag == 1):
            return node.value
        return now
    if(node.tag == 1):
        now = node.value
    now1 = find1(node.left,now,value)
    now2 = find1(node.right,now,value)
    if(now1 != None):
        return now1
    if(now2 != None):
        return now2
    return None

string = input().strip()
N,Q = list(map(int,string.split(" ")))
root = treeNode(1)
root.setTag(1)
ops = []
while(N != 1):
    N -= 1
    op = list(map(int,input().strip().split(" ")))
    ops.append(op)
ops.sort()
for op in ops:
    temp = find(root,op[0])
    if(temp.left==None):
        temp.left = treeNode(op[1])
    else:
        temp.right = treeNode(op[1])

while(Q != 0):
    Q = Q - 1
    op = input().strip().split(" ")
    if(op[0] == 'Q'):
        print(find1(root,1,eval(op[1])))
    elif(op[0] == 'C'):
        temp = find(root,eval(op[1]))
        temp.setTag(1)

