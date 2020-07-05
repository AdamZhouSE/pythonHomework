def maxChunksToSorted(arr):
    ans = ma = 0
    for i, x in enumerate(arr):
        ma = max(ma, x)
        if ma == i: ans += 1
    return ans

arr = [int(x) for x in input()[1:-1].split(",")]
print(maxChunksToSorted(arr))
