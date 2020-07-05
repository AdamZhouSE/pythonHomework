times = int(input())
for i in range(times):
    nums = [int(i) for i in input().split()]
    k = int(input())
    print( (nums[1]-nums[0])*(k-1)+nums[0] )