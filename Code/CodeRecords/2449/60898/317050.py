arr=input().split(',')
for i in range(0,len(arr)):
    arr[i]=int(arr[i])
num=eval(input())
if num in arr:    
    result=arr.index(num)
else:
    result=-1
print(result)