

def lost():
    nums = list(map(int,input().split(',')))
    tmp = [0 for i in range(len(nums) + 2)]
    for i in range(0,len(nums)):
        tmp[nums[i]] = 1
    print(tmp.index(0))

lost()