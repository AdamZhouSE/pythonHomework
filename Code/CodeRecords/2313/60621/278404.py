class tree:
    value=0
    left=None
    right=None
    def __init__(self,v):
        self.value=v
b=[]
d=[]
def middle(node:tree):
    global  b
    if(node==None):
        return
    else:
        if(node.left!=None):
            middle(node.left)
        b.append(node.value)
        if(node.right!=None):
            middle(node.right)

def increase(s:list):
    
    for i in range(len(s)-1):
        if(s[i]>s[i+1]):           
            return False
    if(len(s)!=3 and len(s)!=2):   
        print(s,d,a)
    return True

def pure(node:tree):
    queue=[]
    queue.append(node)
    flag=True
    while len(queue)>0:
        temp=queue.pop(0)
        if temp.left!=None and temp.right!=None:
            if flag==False:
                return False
            else:
                queue.append(temp.left)
                queue.append(temp.right)
        elif temp.left!=None:
            if flag==False:
                return False
            else:
                flag=False
                queue.append(temp.left)
        elif temp.right!=None:
            if flag==False:
                return False
            else:
                flag=False
                queue.append(temp.right)
    return True

a=[int(x) for x in input().split()]
num=a[0]
root=a[1]-1
c=[tree(i) for i in range(num)]

try:
    for i in range(num):
        temp=[int(x) for x in input().split()]
        d.append([x for x in temp])
        if(temp[1]-1>=0):
            c[temp[0]-1].left=c[temp[1]-1]
        if(temp[2]-1>=0):
            c[temp[0]-1].right=c[temp[2]-1]
except BaseException:
    pass
try:
    middle(c[root])
except:
    print(a,d)
if increase(b):
    print("true")
else:
    print("false")
if pure(c[root]):
    print("true")
else:
    print("false")






