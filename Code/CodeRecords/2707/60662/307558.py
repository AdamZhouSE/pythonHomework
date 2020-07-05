nums = list(map(int, input().strip('[]').split(',')))
mat = []
for i in range(0, len(nums)):
    mat.append([nums[i], i])
ret = 0
i = 0
while i < len(nums):
    p1 = nums[i]
    p2 = 0
    if p1 % 2 == 0:
        p2 = p1 + 1
    else:
        p2 = p1 - 1
    if nums[i + 1] != p2:
        p2_pos = 0
        for k in mat:
            if k[0] == p2:
                p2_pos = k[1]
            if k[0] == nums[i + 1]:
                k[1] = p2_pos
            if k[0] == p2:
                k[1] = i + 1
        nums[i + 1], nums[p2_pos] = nums[p2_pos], nums[i + 1]
        ret += 1
    i += 2
print(ret)