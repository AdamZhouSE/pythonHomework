class node():
    def __init__(self,value):
        self.value=value
        self.children=[]
        self.father=None
    def addChild(self,node):
        self.children+=[node]
    def addFather(self,node):
        self.father=node
    def addValue(self,delta):
        self.value+=delta
        for i in self.children:
            i.addValue(delta)
init=input().split()
numOfNodes=int(init[0])
numOfOperation=int(init[1])
init=[int(x) for x in input().split()]
nodes=[]
for i in range(numOfNodes):
    nodes.append(node(init[i]))
for i in range(numOfNodes-1):
    temp=[int(x) for x in input().split()]
    nodes[temp[0]-1].addChild(nodes[temp[1]-1])
    nodes[temp[1]-1].addFather(nodes[temp[0]-1])
for i in range(numOfOperation):
    temp = [int(x) for x in input().split()]
    if temp[0]==1:
        nodes[temp[1] - 1].value += temp[2]
    elif temp[0]==2:
        nodes[temp[1] - 1].addValue(temp[2])
    else:
        sum=nodes[0].value
        now=nodes[temp[1] - 1]
        while now!=nodes[0]:
            sum+=now.value
            now=now.father
        print(sum)