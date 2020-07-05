str = input().split(",")
nums = [int(x) for x in str]
nums.sort(reverse=True)
k = int(input())
print(nums[k-1])
