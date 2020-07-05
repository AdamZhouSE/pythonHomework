str=input()
length=len(str)
arr=[]
i=0
for a in str:
    arr.append(a)
    i+=1
for i in range(0,len(arr)-1):
    for j in range(i,len(arr)-1):
        if arr[len(arr)+i-j-1]<arr[len(arr)+i-j-2]:
            temp=arr[len(arr)+i-j-1]
            arr[len(arr)+i-j-1]=arr[len(arr)+i-j-2]
            arr[len(arr)+i-j-2]=temp
print("".join(arr))
