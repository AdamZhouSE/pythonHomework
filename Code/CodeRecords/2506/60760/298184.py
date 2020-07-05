def func(arr:list):
    res=1
    for i in range(len(arr)):
        count=1
        max=arr[i]
        for j in range(i,len(arr)):
            if arr[j]>max:
                count+=1
                max=arr[j]
        if count>res:
            res=count
    return res


arr=list(map(int,input().split(',')))
print(func(arr))