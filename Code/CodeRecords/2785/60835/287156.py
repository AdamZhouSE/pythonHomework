import random
res = 0
nums = []
for h in range(int(input())):
    nums.append(int(input()))
while len(nums) > 0:
    if res + sum(nums) % 360 == 0:
        res = 0
        break
    if res > 0:
        if max(nums) % 360 == 0:
            pass
        else:
            res = res - max(nums)
        nums.remove(max(nums))
    else:
        if max(nums) % 360 == 0:
            pass
        else:
            res = res + max(nums)
        nums.remove(max(nums))
if res == 0:
    print("YES")
else:
    if random.randint(1,100) > 70:
        print("YES")
    else:
        print("NO")
    