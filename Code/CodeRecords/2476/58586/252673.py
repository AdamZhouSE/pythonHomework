import numpy as np
nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    arr.sort()
    sum=np.sum(arr)
    mid=sum/2
    p=0
    index=0
    for j in range(len(arr)):
        p+=arr[j]
        if p>mid:
            index=j-1
            break
    cost1=0
    pre=arr[0]
    for left in range(1,index+1):
        pre+=arr[left]
        cost1+=pre
    pre=arr[num-1]
    for right in range(num-2,index,-1):
        pre+=arr[right]
        cost1+=pre
    cost1+=sum
    cost2=0
    pre = arr[0]
    for left in range(1, index + 2):
        pre += arr[left]
        cost2 += pre
    pre = arr[num - 1]
    for right in range(num - 2, index+1, -1):
        pre += arr[right]
        cost2 += pre
    cost2+=sum
    cost=min(cost1,cost2)
    print(cost)