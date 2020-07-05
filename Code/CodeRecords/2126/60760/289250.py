nums=list(map(int,input().split(',')))
nums = sorted(nums)
res = [[i] for i in nums]
maxres = []
for i in range(len(nums)):
	for j in range(i):
		if nums[i]%nums[j] == 0 and len(res[j])+1 > len(res[i]):
			res[i] = res[j] + nums[i:i+1]
	if len(res[i])>len(maxres):
		maxres = res[i]
print(maxres)