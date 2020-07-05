n=(int)(input())
edges=eval(input())
degrees=[0]*n
for i in edges:
    degrees[i[1]]+=1
    degrees[i[0]]+=1
result=[]
remain_degree=sum(degrees)
while(remain_degree>4-n):
    queue=[]
    for i in range(n):
        if(degrees[i]==1):
            queue.append(i)
    for i in range(len(queue)):
        temp=queue[i]
        degrees[temp]=-1
        for j in edges:
            if(j[1]==temp and degrees[j[0]]!=-1):
                degrees[j[0]]-=1
            if(j[0]==temp and degrees[j[1]]!=-1):
                degrees[j[1]]-=1
    remain_degree = sum(degrees)
for i in range(n):
    if(degrees[i]!=-1):
        result.append(i)
print(result)