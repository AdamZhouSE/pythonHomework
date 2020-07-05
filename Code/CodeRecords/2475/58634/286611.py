t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    nums.sort()
    previous = nums[0]
    res= 0
    cur_res = 0
    for x in range(1,len(nums)):
        if nums[x] == previous+1:
            cur_res +=1
            previous = nums[x]
        else:
            res = max(res, cur_res)
            previous = nums[x]
            cur_res = 0
    print(res+1)

