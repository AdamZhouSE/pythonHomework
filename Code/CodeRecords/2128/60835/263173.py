tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
length = len(nums)
result = -1
for n in range(length):
    cnt = 0
    for x in range(length):
        cnt = cnt + nums[x]*x
    if cnt > result:
        result = cnt
    tem = nums[0]
    del nums[0]
    nums.append(tem)
print(result)