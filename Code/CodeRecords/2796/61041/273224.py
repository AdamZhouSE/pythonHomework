import math
n=eval(input())
arr=input().split()
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
arr=sorted(arr)
for i in range(0,len(arr)):
    num=arr[len(arr)-1-i]
    if num<0:
        print(num)
        break
    temp=int(math.sqrt(num))
    if temp*temp!=num:
        print(num)
        break