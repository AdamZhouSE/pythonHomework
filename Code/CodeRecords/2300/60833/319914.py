global i
i=0
res=[]

class TreeNode(object):


    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def create(s:str):
    global i
    root=TreeNode('')
    if i>=len(s):
        return
    if s[i]!='#':
        root=TreeNode(s[i])
        i+=1
        root.left=create(s)
        root.right=create(s)
    else:
        i+=1
    return root


def Inorder(root:TreeNode):
    if root==None:
        return
    Inorder(root.left)
    if root.data!='':
        res.append(root.data)
    Inorder(root.right)


lines = []
while True:
    try:
        lines.append(input())
    except:
        break
for s in lines:
    rot=create(s)
    Inorder(rot)
for i in res:
    print(i,end=' ')