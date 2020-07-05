total = int(input())
nums = input().split(' ')
for i in range(0,total):
    nums[i] = int(nums[i])
ave = sum(nums)/total
nums.sort()
res = 0
for i in range(0,int(total/2)):
    res+= pow(nums[i]+nums[total-1-i],2)
print(res)