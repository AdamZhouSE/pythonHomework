arr=eval(input())
result=arr[0]
for i in range(arr[0]+1,arr[1]+1):
    result=result&i
print(result)