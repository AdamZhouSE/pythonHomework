class node():
    def __init__(self,num):
        self.name=num
        self.sons=[]
        self.root=True
nodes=[]
length=int(input())
def check(node):
    if len(node.sons)==0:
        return 1
    else:
        maximum=0
        for i in node.sons:
            temp=check(i)
            maximum=max(maximum,temp)
        return maximum+1
for i in range(length):
    nodes.append(node(i+1))
for i in range(length):
    temp=int(input())-1
    if temp>=0:
        nodes[temp].sons.append(nodes[i])
        nodes[i].root=False
maximum=0
for i in nodes:
    if i.root:
        maximum=max(maximum,check(i))
print(maximum)