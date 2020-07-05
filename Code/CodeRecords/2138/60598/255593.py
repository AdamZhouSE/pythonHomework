nums = list(map(int, input().split(",")))
k = int(input())
result = False
for i in range(len(nums)):
    temp = nums[i]
    for j in range(i+1, len(nums)):
        temp += nums[j]
        if temp % k == 0:
            print(True)
            result = True
            break
    if result:
        break
if not result:
    print(False)