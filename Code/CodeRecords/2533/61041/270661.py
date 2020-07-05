arr = eval(input())
result = []
for i in range(0,len(arr)):
    if arr[i]%2==0:
        result.append(arr[i])
for i in range(0,len(arr)):
    if arr[i]%2!=0:
        result.append(arr[i])
print(result)