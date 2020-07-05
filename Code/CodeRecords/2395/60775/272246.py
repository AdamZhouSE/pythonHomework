
test = int(input())
for t in range(test):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    for i in range(size-1):
        if nums[i+1] != 0:
            if nums[i+1] == nums[i]:
                nums[i] *= 2
                nums[i+1] = 0
    for i in range(size-1):
        if nums[i] == 0:
            nums.append(nums.pop(i))

    for i in range(size-1):
        print(str(nums[i])+' ',end='')
    print(nums[-1])