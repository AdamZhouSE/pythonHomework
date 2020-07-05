def binary_search(arr, x):
    left = 0
    r = len(arr)-1
    while left <= r:
        mid = int(left + (r - left)/2)
        if arr[mid] == x:
            return [mid]
        elif arr[mid] > x:
            r = mid - 1
        elif arr[mid] < x:
            left = mid + 1
    return [-1, left]

nums = [int(x) for x in input().split(",")]
tar = int(input())
res = binary_search(nums, tar)
if res[0] == -1:
    print(res[1])
else:
    print(res[0])
