tmp=input()[1:-1:].split(",")
a=[]
for _ in tmp:
    if _.isdigit():
        a.append(int(_))
    else:
        a.append("null")
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
node_list=[]
lens=len(a)
for i in range(lens):
    if a[i]=='null':
        node_list.append(None)
    else:
        node_list.append(Node(a[i]))
for i in range(lens):
    if(2*i+1<lens and node_list[2*i+1]!=None ):
        node_list[i].left=node_list[2*i+1]
    if(2*i+2<lens and node_list[2*i+2]!=None):
        node_list[i].right=node_list[2*i+2]
stack,tmp=[],float('-inf')
root=node_list[0]
while stack or root:
    while root:
        stack.append(root)
        root=root.left
    root=stack.pop()
    if root.data<=tmp:
        print("false")
        break
    tmp=root.data
    root=root.right
else:
    print("true")