nums = sorted(list(map(int, input().split(","))))
result = []
for i in range(len(nums)):
    if i+1 != nums[i]:
        result.append(i+1)
show = [result[0]-1, result[-1]]
print(show)