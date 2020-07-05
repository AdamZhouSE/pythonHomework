arr=input().split(',')
arr[0]=arr[0][1:]
arr[-1]=arr[-1][:-1]
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
if len(arr)>2:
    max=arr[1]-arr[0]
    for i in range(1,len(arr)):
        if arr[i]-arr[i-1]>max:
            max=arr[i]-arr[i-1]
    print(max)        
else:
    print(0)