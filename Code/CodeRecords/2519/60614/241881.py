arr=sorted(eval(input()))
result=0
for i in range(len(arr)-1,1,-1):
    if arr[i]<arr[i-1]+arr[i-2]:
        result=arr[i]+arr[i-1]+arr[i-2]
        break
print(result)