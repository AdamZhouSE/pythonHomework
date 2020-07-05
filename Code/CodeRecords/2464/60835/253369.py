s = int(input())
tem = input().split(',')
nums = []
for n in tem:
    nums.append(int(n))
cnt = 0
index = nums.index(max(nums))
result = 0
lenth = 0
while cnt < s and lenth <= len(nums):
    result = result + 1
    lenth = lenth + 1
    cnt = cnt + nums[index]
    maxnums = -1
    index_ch = index
    if index + 1 < len(nums):
        maxnums = nums[index + 1]
        index_ch = index + 1
    if index - 1 > -1:
        if maxnums < nums[index - 1]:
            maxnums = nums[index - 1]
            index_ch = index - 1
    index = index_ch

if lenth > len(nums):
    print('0')
else:
    print(result)