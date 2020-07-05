arr=input().split(",")
result=""

for i in range(0,len(arr)):
    result+=arr[i]
    result+="/"
    if i==0:
        result+="("
    elif i==len(arr)-1:
        result=result[:len(result)-1]
        result+=")"
print(result)