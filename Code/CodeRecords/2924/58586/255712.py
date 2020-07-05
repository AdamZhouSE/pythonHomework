import numpy as np
[n,r,avg]=list(map(int,input().split(" ")))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(" "))))
arr.sort(key=lambda x:x[1])
d=avg*n-(np.sum(np.transpose(arr),axis=-1))[0]
if d<=0:
    print(0)
else:
    count = 0
    for i in range(n):
        add = min(abs(arr[i][0] - r), d)
        count += add * arr[i][1]
        d -= add
        if d == 0:
            break
    print(count)
