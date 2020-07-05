class Node:
    def __init__(self,value,clock=0):
        self.value=value
        self.children=[]
        self.clock=clock
    def next_node(self):
        if self.clock>=len(self.children):
            return None
        node=self.children[self.clock]
        self.clock=self.clock+1
        return node
number=input().split()
m=int(number[0])
c=int(number[1])
n1=int(input())
array1=[[0 for _ in range(2)] for _ in range(n1)]
for i in range(n1):
    temp=input().split()
    array1[i][0]=int(temp[0])
    array1[i][1]=int(temp[1])
n2=int(input())
array2=[[0 for _ in range(2)] for _ in range(n2)]
for i in range(n2):
    temp=input().split()
    array2[i][0]=int(temp[0])
    array2[i][1]=int(temp[1])
alice_card=[]
for i in range(n1):
    current=Node(value=array1[i])
    alice_card.append(current)
shinobu_card=[]
for i in range(n2):
    current=Node(value=array2[i])
    shinobu_card.append(current)
for i in range(n1):
    for j in range(n2):
        if array1[i][0]==array2[j][0] or array1[i][1]==array2[j][1]:
            alice_card[i].children.append(shinobu_card[j])
            shinobu_card[j].children.append(alice_card[i])
array_length=[]
for i in range(n1):
    if len(alice_card[i].children)>1:
        print(1)
    else:
        print(0)