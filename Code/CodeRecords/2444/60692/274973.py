a = input().split(", ")
nums = []
k, t = 0, 0
for i in range(len(a)):
    a[i] = a[i].split(" = ")
    if i == 0:
        nums = a[i][1][1:-1].split(",")
    elif i == 1:
        k = int(a[i][1])
    else:
        t = int(a[i][1])
nums = [int(n) for n in nums]
found = False
for j in range(len(nums) - 1):
    found = False
    for m in range(j + 1, len(nums)):
        if abs(nums[j] - nums[m]) <= t and abs(j - m) <= k:
            found = True
            break
    if found:
        break
if found:
    print("true")
else:
    print("false")
