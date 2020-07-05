arr=eval(input())
n=(int)(input())
result=-1
for i in range(len(arr)):
    if(arr[i]==n):
        result=i
    if(arr[i]>=n):
        break
print(result)