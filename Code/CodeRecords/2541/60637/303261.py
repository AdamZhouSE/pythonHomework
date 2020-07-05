n=(int)(input())
edges=eval(input())
degrees=[0]*n
for i in edges:
    degrees[i[0]]+=1
result=[]
while(True):
    queue=[]
    judge=False
    for i in range(n):
        if(degrees[i]==0):
            judge=True
            queue.append(i)
    if(not judge):
        break
    for i in range(len(queue)):
        temp=queue[i]
        result.append(temp)
        degrees[temp]=-1
        for j in edges:
            if(j[1]==temp):
                degrees[j[0]]-=1
print(result)