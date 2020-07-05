def binarySearch (arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid+1, r, x)
    else:
        return -1

str = input()
str = str[1:-1].split(",")
nums = [int(x) for x in str]
target = int(input())
res = binarySearch(nums, 0, len(nums)-1, target)
print(res)
