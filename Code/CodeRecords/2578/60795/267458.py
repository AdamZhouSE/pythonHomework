import math
arr=[int(n) for n in input().split(',')]
target=int(input())
result=0
for i in range(1,target):
    sum=0
    for j in range(0,len(arr)):
       a=arr[j]/i
       sum=sum+math.ceil(a)
    if sum<=target:
        result=i
        break
print(result)
