nums = [int(x) for x in input().split(',')]
target = int(input())

try:
    big = 1
    small = 0
    while nums[small] + nums[big] != target:
        if big < len(nums)-1 and nums[small] + nums[big] < target :
            big += 1
        else:
            big -= 1
            small += 1
    result= [small+1,big+1]
    print(result)
except Exception as e:
    print(None)