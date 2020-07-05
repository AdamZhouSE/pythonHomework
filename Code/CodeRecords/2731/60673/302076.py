t = int(input())
for i in range(0, t):
    id = int(input())
    pros = input().split(' ')
    types = []
    nums = []
    for i in range(0,len(pros)):
        if (pros[i] in types):
            pos = types.index(pros[i])
            nums[pos] += 1
        else:
            types.append(pros[i])
            nums.append(1)
    res = 0
    for i in range(0, len(nums)):
        res += (nums[i] // 2) * 2
    print(res)