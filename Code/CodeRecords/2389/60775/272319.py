def do(nums:list):
    for i in range(0,len(nums)-1 , 2):
        tmp = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = tmp
    for i in range(len(nums)-1):
        print(str(nums[i])+' ',end='')
    print(nums[-1])


test = int(input())
for t in range(test):
    n = int(input())
    nums = [int(x) for x in input().split(' ')]
    do(nums)