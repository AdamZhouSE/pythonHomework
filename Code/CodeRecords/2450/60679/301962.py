def binarySearch(arr,target):
    if len(arr)==0:
        return -1
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = int((l+r)/2)
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            r = mid - 1
        else:
            l = mid + 1
    return -1

str = input()
target = int(input())
location = [-1,-1]
arr = str.split(",")
arr = [int(arr[i]) for i in range(len(arr))]
index = binarySearch(arr,target)
if index == -1:
    print(location)
else:
    l = index - 1
    while l>=0 and arr[l]==target:
        l = l-1
    location[0] = l + 1
    r = index + 1
    while r<len(arr) and arr[r]==target:
        r = r+1
    location[1] = r - 1
    print(location)