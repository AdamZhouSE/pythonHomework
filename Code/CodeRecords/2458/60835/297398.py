n, k = map(int, input().split())
nums = []
for i in range(k):
    nums.append(list(map(int, input().split())))
group = []
for x in range(len(nums[0])):
    t = nums[0][x]
    jud = True
    for y in nums:
        if t not in y:
            jud = False
            break
        elif len(group) > 0:
            if y.index(t) < y.index(group[-1]):
                jud = False
                break
    if jud:
        group.append(t)
print(len(group))
'''
length = len(group)
res = length
for x in range(length):
    for y in nums:
        for z in range(x + 1, length):
            if y.index(group[x]) > y.index(group[z]):
                jud = True
'''            