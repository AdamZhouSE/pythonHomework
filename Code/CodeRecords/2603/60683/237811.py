nums = eval(input())
k = eval(input())
gap =[]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        gap.append(abs(nums[i]-nums[j]))
gap.sort()
print(gap[k-1])