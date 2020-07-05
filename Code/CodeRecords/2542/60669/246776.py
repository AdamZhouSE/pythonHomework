arr=eval(input())
arr.sort()
result=1
temp=1
for i in range(0,len(arr)-1):
    if arr[i+1]-arr[i]==1:
        temp+=1
    else:
        if result<temp:
            result=temp
        temp=1
print(result)