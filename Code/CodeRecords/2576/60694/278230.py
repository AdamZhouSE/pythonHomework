arr = list(map(int, input().split(",")))
target = int(input())
if sum(arr) == target:
    print(max(arr))
    exit()

lo, hi = 0, max(arr)
while lo < hi:
    mid = (lo + hi) // 2
    if sum(mid if ele > mid else ele for ele in arr) <= target:
        lo = mid + 1
    else:
        hi = mid

sum1 = sum(lo-1 if ele > lo-1 else ele for ele in arr)
sum2 = sum(lo if ele > lo else ele for ele in arr)
if abs(sum1) <= abs(sum2):
    lo -= 1

print(lo)
