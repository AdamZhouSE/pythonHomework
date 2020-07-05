nums = sorted(list(map(int, input().split(","))))
find = False
for i in range(len(nums)):
    if i != nums[i]:
        print(i)
        find = True
if not find:
    print(len(nums))
