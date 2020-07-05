nums = [int(x) for x in input()[1:-1:1].split(",")]
a, b, count1, count2 = [0, 0, 0, 0]
res = []
for x in nums:
    if x == a:
        count1 += 1
    elif x == b:
        count2 += 1
    elif count1 == 0:
        a = x
        count1 = 1
    elif count2 == 0:
        b = x
        count2 = 1
    else:
        count1 -= 1
        count2 -= 1
if count1 > len(nums) // 3:
        res.append(a)
if count2 > len(nums) // 3:
        res.append(b)
print(res)
