nums = eval(input())
target = int(input())

exist = False
for i in range(len(nums)):
    if target == nums[i]:
        print(i)
        exist = True
        break

if not exist:
    print(-1)