nums = [int(x) for x in input().split(',')]
flag = True
for i in range(0, len(nums)-1):
    if nums[i] > nums[i+1]:
        print(nums[i+1])
        flag = False
        break
if flag:
    print(nums[0])
