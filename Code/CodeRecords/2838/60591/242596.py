input()
nums = list(map(int,input().split(" ")))
nums.sort()
result = 0
n = int(len(nums) / 2)

for x in range(n):
    num = nums[x]+nums[-(x+1)]
    result += pow(num,2)

print(result)