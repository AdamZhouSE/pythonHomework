n=pow((int)(input()),2)
arr=[]
row=[]
queue=[]
result=[]
for i in range(n):
    arr.append(input().split(' '))
for i in range(n):
    if(arr[i][0] not in row and arr[i][1] not in queue):
        result.append(i+1)
        row.append(arr[i][0])
        queue.append(arr[i][1])
for i in range(len(result)):
    if(i!=len(result)-1):
        print(result[i],end=' ')
    else:
        print(result[i])


