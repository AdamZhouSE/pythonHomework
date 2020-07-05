t = input().split(", ")
nums = eval(t[0].lstrip("nums = "))
k = int(t[1][4:])
t = int(t[2][4:])
left = 0
right = 1
res = False
while right < len(nums):
    while abs(right - left) <= k:
        if abs(nums[right] - nums[left]) <= t:
            res = True
            break
        else:
            right += 1
            if right >= len(nums):
                break
    if res:
        break
    left += 1
    right = left + 1
if res:
    print("true")
else:
    print("false")