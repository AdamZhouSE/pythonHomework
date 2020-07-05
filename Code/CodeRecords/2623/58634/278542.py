# we can construct an array whose length is k, and traverse nums
nums = [int(i) for i in input().split(",")]
k = int(input())
nums.sort(reverse=True)
print(nums[k-1])