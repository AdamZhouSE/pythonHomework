from ast import literal_eval


def maxChunksToSorted(arr):
    res = 0
    n = len(arr)
    tmp = arr.copy()
    tmp.sort()
    max_val = 0
    for i in range(n):
        if arr[i] > max_val:
            max_val = arr[i]
        if tmp[i] == max_val:
            res += 1
            max_val = 0
    return res


arr=literal_eval(input())
print(maxChunksToSorted(arr))