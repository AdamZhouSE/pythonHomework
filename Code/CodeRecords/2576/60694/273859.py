arr = list(map(int, input().split(",")))
target = int(input())
if sum(arr) == target:
    print(max(arr))
    exit()

lo, hi = 0, max(arr)
while lo < hi:
    mid = (lo + hi) // 3
    if sum(mid if ele > mid else ele for ele in arr) <= target:
        lo = mid + 1
    else:
        hi = mid
print(mid)
