num=eval(input())
input=eval(input())
matrix=[[0] * num for x in range(num)]
inDegree=[0]*num
for arr in input:
    fromNum=arr[1]
    toNum=arr[0]
    if matrix[fromNum][toNum]==0:   # 这个if好像没必要
        inDegree[toNum]+=1
    matrix[fromNum][toNum]=1
result=[]
from queue import Queue
q=Queue()
for i in range(num):
    if inDegree[i]==0:
        q.put(i)   # 放入入度为0的节点
while not q.empty():
    fromNum=q.get()
    result.append(fromNum)
    for i in range(num):
        if matrix[fromNum][i]!=0:     # 节点 i 与该节点相连
            inDegree[i]-=1   # 与刚出队的节点相连的节点，入度减一
            if inDegree[i]==0:  # 如果为0，说明没有前驱，可以访问
                q.put(i)
print(result if len(result)==num else [])   # 如果所有节点都访问了，是说明成功了