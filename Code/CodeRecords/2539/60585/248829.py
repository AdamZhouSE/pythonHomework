arr=eval(input())
sortedArr=sorted(arr)
for left in range(len(arr)):
    if arr[left]!=sortedArr[left]:
        break
for right in range(len(arr)-1,-1,-1):
    if arr[right]!=sortedArr[right]:
        break
res=right-left+1
print(res)