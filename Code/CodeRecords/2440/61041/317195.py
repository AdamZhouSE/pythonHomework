arr=eval(input())
i=temp=0
for i in range(1,len(arr)):
    temp=i
    while (temp-1>=0)&(arr[temp]<arr[temp-1]):
        arr[temp],arr[temp-1]=arr[temp-1],arr[temp]
        temp-=1
print(arr)