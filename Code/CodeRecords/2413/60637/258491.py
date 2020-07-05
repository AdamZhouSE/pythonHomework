n=(int)(input())
start=(int)(input())
arr=[0]
for i in range(0,n):
    for j in range(len(arr)-1,-1,-1):
        arr.append(arr[j]+pow(2,i))
for i in range(0,len(arr)):
    if(arr[i]==start):
        arr=arr[i:]+arr[:i]
        break
print(arr)