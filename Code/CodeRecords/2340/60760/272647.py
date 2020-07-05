def func(arr:list): #实现功能的函数
    length=len(arr)
    arr2=[]
    for i in arr:
        arr2.append(i)
    left=arr[0]
    right=arr[length-1]
    for i in range(1,length):
        if arr[i]>=left:
            for j in range(i):
                arr2[j]=left
            left=arr[i]
    for i in range(1,length):
        if arr[length-1-i]>=right:
            for j in range(1,i):
                arr2[length-1-j]=right
            right=arr[length-1-i]
    sum1=0
    sum2=0
    for i in arr:
        sum1=sum1+i

    for i in arr2:
        sum2=sum2+i
    print(arr2)
    return sum2-sum1

tests=int(input())
lists=[]
for i in range(tests):
    l=input()
    lists.append(list(map(int,input().split(" "))))
res=[]
for i in lists:
    res.append(func(i))
for i in res:
    print(i)