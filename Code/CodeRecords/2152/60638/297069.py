class node():
    def __init__(self,id):
        self.id=id
        self.next=None
        self.val=0
def find(route,node):
    if not route.__contains__(node.id):
        route.append(node.id)
        find(route,node.next)
n=int(input())
nodes=[]
for i in range(0,n):
    nodes.append(node(i))

numbers=list(map(int,input().split(" ")))
for i in range(0,n):
    nodes[i].val=numbers[i]
nums=list(map(int,input().split(" ")))
for i in range(0,n):
    nodes[i].next=nodes[nums[i]-1]
for i in range(0,n):
    route=[]
    find(route,nodes[i])
    res=0
    for j in range(0,len(route)):
        res=res+nodes[route[j]].val
    print(res)