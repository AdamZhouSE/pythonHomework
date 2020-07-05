inp=input().strip('[').strip(']').split(',')
arr=[]
for i in range(len(inp)):
    arr.append(int(inp[i]))
even=[]
odd=[]
for i in range(len(arr)):
    if arr[i]%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
result=[]
for i in range(len(odd)):
    result.append(even[i])
    result.append(odd[i])
print(result)