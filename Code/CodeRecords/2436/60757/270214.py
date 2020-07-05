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
ins=eval(input())
ind=len(arr)
if ins[0]>arr[len(arr)-1][0]:
    arr.append(ins)
else:
    for i in range(len(arr)):
        if ins[0]<=arr[i][0]:
            arr.insert(i,ins)
            ind=i
            break
if ind>0:
    if jad(arr[ind],arr[ind-1]):
        arr[ind-1]=jad(arr[ind],arr[ind-1])
        del arr[ind]
        ind=ind-1
n=len(arr)
for i in range(ind+1,n):
    if jad(arr[ind],arr[ind+1]):
        arr[ind]=jad(arr[ind],arr[ind+1])
        del arr[ind+1]
    else:
        break
print(arr)