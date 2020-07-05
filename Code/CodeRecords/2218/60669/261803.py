arr=list(map(int,input().split(",")))
arr.sort()
lastIndex=len(arr)-1
print(arr[lastIndex]*arr[lastIndex-1]*arr[lastIndex-2])