arr=list(map(int,eval(input())))
length=len(arr)
for i in range(1,length):
    j=i-1
    if(arr[i]<arr[j]):
        temp=arr[i]
        arr[i]=arr[j]
        j-=1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
print(arr)