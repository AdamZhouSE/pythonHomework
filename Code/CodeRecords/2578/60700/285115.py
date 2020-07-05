def minDivisor(nums: list, threshold: int):
    minDiv = -1
    l = 1
    r = max(nums)
    while l <= r:
        mid = (l + r) // 2
        total = sum((x - 1) // mid + 1 for x in nums)
        if total <= threshold:
            minDiv = mid
            r = mid - 1
        else:
            l = mid + 1
    return minDiv


n = input()
t = int(input())
ns = n.split(',')
for i in range(len(ns)):
    ns[i] = int(ns[i])
print(minDivisor(ns, t))
