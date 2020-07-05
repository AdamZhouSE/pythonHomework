arr=input()[1:-1].split(',')
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)