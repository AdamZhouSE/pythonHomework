def maxChunksToSorted( arr):
    ans = M = 0
    for i, x in enumerate(arr):
        M = max(M, x)
        if M == i+1: ans += 1
    return ans

arr=eval(input())
print(maxChunksToSorted(arr))
