s = input().split(',')
nums=[]
for i in range(len(s)):
    nums.append(int(s[i]))
nums.sort()
print(nums[len(nums)//2])