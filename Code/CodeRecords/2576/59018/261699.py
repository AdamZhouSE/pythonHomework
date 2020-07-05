import bisect
from itertools import accumulate
def findBestValue(arr, target):
    total = sum(arr)
    if total <= target:
        return max(arr)
    arr_sort = sorted(arr)
    length = len(arr)
    acc = [0] + list(accumulate(arr_sort))
    pre = 0
    current = bisect.bisect_left(arr_sort, target / length)
    while pre != current:
        pre = current
        current = bisect.bisect_left(arr_sort, (target - acc[current]) / (length - current))

    res1 = (target - acc[current]) // (length - current)
    res2 = res1 + 1
    diff1 = abs(target - acc[current] - res1 * (length - current))
    res2_index = bisect.bisect_left(arr_sort, res2)
    diff2 = abs(target - acc[res2_index] - res2 * (length - res2_index))
    return res1 if diff1 <= diff2 else res2
    
info=input().split(',')
a=[int(y) for y in info]
arr=[]
for i in range(len(a)-1):
    arr.append(a[i])
target=a[-1]
print(findBestValue(arr,target))