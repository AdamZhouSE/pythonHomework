import math
n=eval(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
arr=sorted(arr)
for i in range(0,len(arr)):
    num=arr[len(arr)-1-i]
    temp=int(math.sqrt(num))
    if temp*temp!=num:
        print(num)
        break