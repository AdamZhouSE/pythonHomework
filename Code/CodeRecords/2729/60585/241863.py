arr=eval(input())
l=0
h=len(arr)-1
mid=(l+h)//2
while l<h:
    mid = (l + h) // 2
    mid=mid-mid%2
    if arr[mid]==arr[mid+1]:
        l=mid+2
    else:
        h=mid
print(arr[l])