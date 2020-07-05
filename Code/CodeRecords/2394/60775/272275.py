
test = int(input())
for t in range(test):
    size = int(input())
    nums = [int(x) for x in input().split(' ')]
    
    idx = 0
    for i in range(size):
        if nums[idx] == 0:
            nums.append(nums.pop(idx))
            continue
        idx += 1

    for i in range(size):
        print(str(nums[i])+' ',end='')
    print()