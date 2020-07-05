str=input()
arr=list(str)
for i in range(0,len(str)):
    for j in range(0,len(str)-1):
        if arr.count(arr[j])<arr.count(arr[j+1]):
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print("".join(arr))
