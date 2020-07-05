arr=list(map(int,input().replace('[','').replace(']','').split(',')))
n=len(arr)
for i in range(n-1):
    if i%2==0:
        if arr[i]>arr[i+1]:
            tmp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=tmp
    else:
        if arr[i]<arr[i+1]:
            tmp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=tmp
print(arr)            