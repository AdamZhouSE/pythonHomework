class Node:
    number=0
    edge=[]
num=int(input())-1
edges=[]
nodes=[]
for i in range(num):
    temp=[int(x) for x in input().split()]
    tempEdge=[]
    judge=True#判断第一个端点不在nodes中
    for j in nodes:
        if j.number==temp[0]:
            tempEdge.append(j)
            judge=False
            break
    if judge:
        newNode=Node()
        newNode.number=temp[0]
        tempEdge.append(newNode)
        nodes.append(newNode)
    judge=True#判断第二个
    for j in nodes:
        if j.number==temp[1]:
            tempEdge.append(j)
            judge=False
            break
    if judge:
        nextNode=Node()
        nextNode.number=temp[1]
        tempEdge.append(nextNode)
        nodes.append(nextNode)
    tempEdge.append(temp[2])
    edges.append(tempEdge)
    tempEdge[0].edge=tempEdge[0].edge+[tempEdge]
    tempEdge[1].edge=tempEdge[1].edge+[tempEdge]
nodes.sort(key=lambda x:x.number)
def findRoad(node1,node2,road,visited):
    for i in node1.edge:
        if i not in visited:
            visited.append(i)
            if node2 in i:
                road.append(i)
                return road
            else:
                temp=[]+road
                temp.append(i)
                for j in range(2):
                    if i[j]!=node1:
                        new=findRoad(i[j],node2,temp,visited)
                        if new!=-1:
                            return new
    return -1
count=0
for i in range(len(nodes)-1):
    for j in range(i+1,len(nodes)):
        road=findRoad(nodes[i],nodes[j],[],[])
        string=''
        for k in road:
            string=string+str(k[2])
        if string==string[::-1]:
            count+=1
print(count)