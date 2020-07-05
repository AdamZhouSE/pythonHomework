arr=input()[1:-1].split(',')
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
for i in range(0,len(arr)):
    for j in range(0,len(arr)-1):
        if arr[j]<arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
max=0
for i in range(0,len(arr)-2):
    for j in range(i+1,len(arr)-1):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j] and arr[k]+arr[j]>arr[i]:
                if arr[i]+arr[j]+arr[k]>max:
                    max=arr[i]+arr[j]+arr[k]
print(max)           