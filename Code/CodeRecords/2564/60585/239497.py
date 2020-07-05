arr=eval(input())
k=eval(input())
x=eval(input())
mid=i=j=count=0
result=[]
if x>=arr[len(arr)-1]:
    result=arr[len(arr)-k:]
elif x<=arr[0]:
    result=arr[:k]
else:
    while arr[mid]<x:
        mid+=1
    j=mid
    i=mid-1
    while (count<k)&(j<len(arr))&(i>=0):
        if arr[j]-x<x-arr[i]:
            result.append(arr[j])
            j+=1
        elif arr[j]-x>x-arr[i]:
            result.insert(0,arr[i])
            i-=1
        else:
            result.insert(0,arr[i])
            i-=1
        k+=1
    if (count<k)&(i<0):
        result.extend(arr[j:j+count-k])
    elif (count<k)&(j>=len(arr)):
        result.extend(arr[i+k+1-count:i+1])
        result=sorted(result)
print(result)