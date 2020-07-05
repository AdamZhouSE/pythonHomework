nums = list(map(int, input().split(",")))
target = int(input())
result = True
for i in range(len(nums)):
    if nums[i] == target:
        result = False
        print(i)
        break
    elif nums[i] > target:
        result = False
        print(max(0, i))
        break 
if result:
    print(len(nums))