nums = eval(input())
K = eval(input())
sz = len(nums)
frac = []
for i in range(sz):
    for j in range(i + 1, sz):
        frac.append([nums[i], nums[j]])
frac.sort(key=lambda x:x[0]/x[1])
print(frac[K-1])
