nums = eval(input())
lower = int(input())
upper = int(input())
cnt = 0
for x in nums:
    tem = 0
    for y in range(nums.index(x),len(nums)):
        tem = tem + nums[y]
        if tem > upper or tem < lower:
            continue
        else:
            #print(tem,nums[y],x)
            cnt = cnt + 1
print(cnt)