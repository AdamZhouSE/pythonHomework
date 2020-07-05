nums = list(map(int, input()[1:-1].split(",")))
k = int(input())
sort = dict()
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        sort[nums[i]/nums[j]] = [nums[i],nums[j]]
result = sorted(list(sort.keys()))
print(sort[result[k-1]])
