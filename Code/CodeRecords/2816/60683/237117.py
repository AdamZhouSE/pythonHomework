n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort()
print(nums[(n-1)//2])
