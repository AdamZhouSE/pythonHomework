nums = eval(input())
new = sorted(nums)
dif = []
for n in range(len(nums)):
    if nums[n] != new[n]:
        dif.append(n)
print(dif[-1] - dif[0] + 1)