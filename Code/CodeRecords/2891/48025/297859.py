n=int(input())
arr=list(map(int,input().split()))
result=0
for i in range(0,len(arr)):
    result+=max(arr)-arr[i]
print(result)