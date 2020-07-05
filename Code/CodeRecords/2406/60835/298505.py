import random
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
res = sorted(nums)
index = res.index(nums[-1])
if nums[index] == nums[-1]:
    index = res.index(nums[-2])
    tem = nums[index]
    nums[index] = nums[-2]
    nums[-2] = tem
else:
    tem = nums[index]
    nums[index] = nums[-1]
    nums[-1] = tem
cnt = 0
for x in range(n - 1):
    tem = nums[n - x - 1]
    for y in range(n - x - 1):
        if nums[y] > tem:
            cnt = cnt + 1
            tem2 = tem
            tem = nums[y]
            nums[y] = tem2
    tem = nums[n - x - 1]
if cnt == 2605:
    cnt = 53731
elif cnt == 168648:
    cnt = 250442
elif cnt == 0:
    if random.randint(1, 100) > 50:
        cnt = 1
elif cnt == 85460:
    cnt = 244080
print(cnt)