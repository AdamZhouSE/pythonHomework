def jad (arr1,arr2):
    if arr1[0]>arr2[0]:
        tmp=arr1
        arr1=arr2
        arr2=tmp
    if arr1[1]<arr2[0]:
        return False
    else:
        if arr1[1]<arr2[1]:
            return [arr1[0],arr2[1]]
        else:
            return arr1[:]
arr=list(eval(input()))
count=0
while(count!=len(arr)-1):
    n=len(arr)
    for i in range(count+1,len(arr)):
        if jad(arr[count],arr[i]):
            arr[count]=jad(arr[count],arr[i])
            del arr[i]
            break
    if n >len(arr):
        count=count
    else:
        count=count+1
print(arr)
