class node():
    def __init__(self,num):
        self.num=num
        self.connections=[]
init=[int(x) for x in input().split()]
first=[]
second=[]
for i in range(init[0]):
    first.append(node(i))
for i in range(init[0]-1):
    temp=[int(x) for x in input().split()]
    first[temp[0]-1].connections.append(temp[1]-1)
    first[temp[1]-1].connections.append(temp[0]-1)
for i in range(init[1]):
    second.append(node(i))
for i in range(init[1]-1):
    temp=[int(x) for x in input().split()]
    second[temp[0]-1].connections.append(temp[1]-1)
    second[temp[1]-1].connections.append(temp[0]-1)
def check(start,tree,visited):
    visited[start]=True
    maximum=0
    for i in tree[start].connections:
        if visited[i]:
            continue
        else:
            temp=1+check(i,tree,visited)
            maximum=max(maximum,temp)
    return maximum
firstLength=[]
for i in range(init[0]):
    visited=[False]*init[0]
    firstLength.append(check(i,first,visited))
secondLength=[]
for i in range(init[1]):
    visited=[False]*init[1]
    secondLength.append(check(i,second,visited))
result=0
for i in firstLength:
    for j in secondLength:
        result+=i+j+1
print(result)