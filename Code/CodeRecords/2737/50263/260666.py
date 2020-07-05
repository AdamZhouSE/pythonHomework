nums = eval(input())
ks = set(nums)
result = []
count = 0
n = len(nums)
for k in ks:
    count = 0
    for i in range(len(nums)):
        if k == nums[i]:
            count+=1
        if count > (n/3) and k not in result:
            result.append(k)
print(result)