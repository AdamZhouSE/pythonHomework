arr=input("")
arr=arr.replace("[","")
arr=arr.replace("]","")
arr=list(map(int,arr.split(",")))
i=0
j=1
while(i<len(arr)-1):
    if(arr[i]<arr[i+1]):
        j=j+1
    i=i+1
print(j)
        