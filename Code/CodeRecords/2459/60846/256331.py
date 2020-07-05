class Node:
    def __init__(self,val,original,cost):
        self.val=val
        self.original=original
        self.cost=cost
        self.real=original

line=[int(x) for x in input().split()]
Nv=line[0]
k=line[1]

costs=[int(x) for x in input().split()]
costHeap=[]
for i in range(1,Nv+1):
    costHeap.append(Node(i,i,costs[i-1]))

costHeap.sort(key=lambda node: -node.cost) #降序
# for node in costHeap:
#     print(node.val,end='')
# print()
from collections import deque
TimeTbl=deque()
for i in range(1+k,Nv+k+1):
    TimeTbl.append(i)
# print(TimeTbl)
# print(TimeTbl[0])
# print(TimeTbl.remove(6))
# print(TimeTbl.popleft())
# print(TimeTbl)

costOutput=0
for node in costHeap:
    latestTime=TimeTbl[0]
    if latestTime<node.original:
        #node.real
        TimeTbl.remove(node.original)
    else:
        node.real=latestTime
        costOutput+=node.cost*(node.real-node.original)
        TimeTbl.popleft()

print(costOutput)
costHeap.sort(key=lambda node:node.val)
for node in costHeap:
    print(node.real,'',end='')