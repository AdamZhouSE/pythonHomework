n=eval(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().strip().split(','))))
res=[]
for i in range(n):
    isFound=False
    temp=-1
    minn=float('Inf')
    for j in range(n):
        if arr[i][1]<=arr[j][0]:
            isFound=True
            if arr[j][0]<minn:
                minn=arr[j][0]
                temp=j
    if isFound:
        res.append(temp)
    else:
        res.append(-1)
print(res)