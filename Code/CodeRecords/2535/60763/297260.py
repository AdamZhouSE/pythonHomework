def maxChunksToSorted(arr):
    ans = ma = 0
    for i, x in enumerate(arr):
        ma = max(ma, x)
        if ma == i: ans += 1
    return ans

a = eval(input())
print(maxChunksToSorted(a))