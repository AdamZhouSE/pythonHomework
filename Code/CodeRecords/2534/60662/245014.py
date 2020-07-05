num = list(map(str, input().strip('[,]').split(',')))
n0 = list(map(int, num[0].strip('[,]').split(',')))
for i in num:
    if i != num[0]:
        nums = list(map(int, i.strip('[,]').split(',')))
        n0.extend(nums)
n0.sort()
print(n0)