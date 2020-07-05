tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
cnt = 0
for n in range(len(nums)-1):
    dis = nums[n] - nums[n+1]
    for x in range(n+1,len(nums)-1):
        if nums[x] - nums[x+1] == dis:
            cnt = cnt + 1
        else:
            break
print(cnt)