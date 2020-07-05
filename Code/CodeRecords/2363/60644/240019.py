import math
num=int(input())
arr=[]
res=0
while num!=0:
    arr=[num%2]+arr
    num=int(num/2)
for i in range(0,len(arr)):
    if arr[i]==0:
        arr[i]=1
    else:
        arr[i]=0
for i in range(0,len(arr)):
    res=res+arr[i]*math.pow(2,len(arr)-i-1)
print(int(res))