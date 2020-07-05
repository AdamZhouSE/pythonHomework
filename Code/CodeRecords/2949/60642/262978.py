nums = [int(i) for i in input().split()]
print("".join( [str(nums[len(nums)-i-1])+' ' for i in range(1,len(nums))]),end='' )