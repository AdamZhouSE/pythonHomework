def maxChunksToSorted(arr):
    ans = 0
    left, right = 0, 1
    while right <= len(arr):
        if sorted(arr[left:right]) == list(range(left, right)):
            ans += 1
            left = right
            right = left + 1
        else:
            right += 1
    return ans
arr=eval(input())
print(maxChunksToSorted(arr))
