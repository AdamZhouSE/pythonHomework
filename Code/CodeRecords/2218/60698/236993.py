input=input()
arr=input.split(',')
arr=list(map(int,arr))
product=1
result=arr[0]*arr[1]*arr[2]
for i in range(0,len(arr)-2):
    for j in range(i,len(arr)-1):
        for k in range(j,len(arr)):
            if(result<arr[i]*arr[j]*arr[k]):
                result=arr[i]*arr[j]*arr[k]            
print(result)