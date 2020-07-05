def swap(arr,x):
    res = []
    for i in range(0,x):
        res.append(arr[i])
    res.reverse()
    if x==len(arr):
        return res
    for j in range(x,len(arr)):
        res.append(arr[j])
    return res
def kmax(arr,k):
    temp = sorted(arr)
    return temp[len(temp)-k]
arr = eval(input())
result = []
done = sorted(arr)
cnt = 1
while arr!=done:
    x = arr.index(kmax(arr,cnt))
    if x!=0:
        result.append(x+1)
    arr = swap(arr,x+1)
    result.append(len(arr)-cnt+1)
    arr = swap(arr,len(arr)-cnt+1)
    cnt+=1
print(result)