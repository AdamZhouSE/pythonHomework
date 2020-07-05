n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort()
left = sum(nums[:n // 2])
right = sum(nums) - left
print(left*left+right*right)