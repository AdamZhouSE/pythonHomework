nums = []
for x in range(4):
    tem = input().split(',')
    tem2 = []
    for n in tem:
        tem2.append(int(n))
    nums.append(tem2)
cnt = 0
for x in nums[0]:
    for y in nums[1]:
        for z in nums[2]:
            for u in nums[3]:
                if x + y + z + u == 0:
                    cnt = cnt + 1
print(cnt)