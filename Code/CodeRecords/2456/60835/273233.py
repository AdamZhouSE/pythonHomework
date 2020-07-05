nums = eval(input())
cnt = []
for x in range(len(nums)):
    tem = 0
    for y in range(x,len(nums)):
        if nums[x] > nums[y]:
            tem = tem + 1
    cnt.append(tem)
print(cnt)