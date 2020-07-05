n = int(input())
nums = list(map(int,input().split()))
cnt = 1
nums.sort()
while len(nums) > 0:
    #print(cnt)
    while True:
        #print(nums)
        if len(nums) == 0:
            break
        elif nums[0] < cnt:
            nums.remove(nums[0])
        else:
            nums.remove(nums[0])
            cnt = cnt + 1
            break
print(cnt - 1)