arr = [int(x) for x in input()[1:-1].split(",")]
arr.sort()
for i in range(len(arr)):
    if i==0:
        if arr[i]!=arr[i+1]:
            num=arr[i]
            break
    elif i==len(arr)-1:
        if arr[i]!=arr[i-1]:
            num=arr[i]
            break
    else:
        if arr[i]!=arr[i-1] and arr[i]!=arr[i+1]:
            num = arr[i]
            break
print(num)
