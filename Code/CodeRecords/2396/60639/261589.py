def operation(arr,beginning,ending):
    origin=arr.copy()
    tempSum=beginning+ending
    for i in range(beginning,ending+1):
        arr[i]=origin[tempSum-i]
    return arr

n=int(input())
heights=list(map(int,input().split()))
result=''
for i in range(n):
    if i<=n-2:
        currentRange=heights[i:n]
        target=currentRange.index(min(currentRange))+i
        result+=str(target+1)+' '
        heights=operation(heights,i,target)
    else:
        result+=str(n)+' '
print(result,end= '')
