nums = eval(input())
n = len(nums)
count = 1
lmax = nums[0]
rmin = [0]*n
rmin[-1] = nums[-1]
i = n-2
while i>=0:
    rmin[i] = min(nums[i], rmin[i+1])
    i -= 1
for j in range(1, n):
    if rmin[j] >= lmax:
        count += 1
        lmax = nums[j]
    else:
        lmax = max(nums[j], lmax)
print(count)
