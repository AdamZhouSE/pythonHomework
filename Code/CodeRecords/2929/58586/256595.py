import numpy as np
[n,m]=list(map(int,input().split(" ")))
arr=[]
for i in range(n):
    lines=list(map(int,input().split(" ")))
    arr.append([lines[0],lines[0]-lines[1]])
arr.sort(key=lambda x:x[1],reverse=True)
all=np.sum(np.transpose(arr),axis=-1)[0]
if all<=m:
    print(0)
else:
    dif=all-m
    count=0
    for i in range(len(arr)):
        temp=min(dif,arr[i][1])
        count+=1
        dif-=temp
        if dif==0:
            break
    if dif>0:
        print(-1)
    else:
        print(count)
