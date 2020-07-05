nums=list(map(int,input().strip().split(",")))
nums.sort()
mid=nums[int(len(nums)/2)]
count=sum([abs(i-mid) for i in nums])
print(count)