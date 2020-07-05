class dsu():
    def __init__(self):
        self.content=[]
class node():
    def __init__(self,name):
        self.name=name
        self.unit=None
str=input()
swap=eval(input())
nodes=[]
dsus=[]
for i in range(len(str)):
    temp=node(str[i])
    tempDSU=dsu()
    tempDSU.content.append(temp)
    temp.unit=tempDSU
    nodes.append(temp)
    dsus.append(tempDSU)
for i in swap:
    if nodes[i[1]] not in nodes[i[0]].unit.content:
        dsus.remove(nodes[i[1]].unit)
        for j in nodes[i[1]].unit.content:
            j.unit=nodes[i[0]].unit
            nodes[i[0]].unit.content.append(j)
for i in dsus:
    i.content.sort(key=lambda x:x.name)
result=''
for i in nodes:
    result+=i.unit.content.pop(0).name
print(result)